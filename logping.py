import pandas as pd
import time
import json
import requests
import datetime
import logging
import sys
from misc import get_header, get_json
from datetime import timedelta
from message import telegram_send_message
from binance import get_position, get_nickname, get_markprice

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)

# Load UIDs dari file JSON
def load_uids():
    try:
        with open('uids.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("File uids.json tidak ditemukan. Jalankan setup.py terlebih dahulu.")
        sys.exit(1)
    except json.JSONDecodeError:
        logging.error("Format uids.json tidak valid.")
        sys.exit(1)

TARGETED_ACCOUNT_UIDs = load_uids()

ACCOUNT_INFO_URL_TEMPLATE = 'https://www.binance.com/en/futures-activity/leaderboard/user?encryptedUid={}'

# Modifying DataFrame, including calculating estimated entry size in USDT
def modify_data(data) -> pd.DataFrame:
    """
    Memproses data posisi trading dari API terbaru Binance.
    
    Parameters:
        data (dict): Data mentah dari API Binance.
    
    Returns:
        pd.DataFrame: DataFrame yang berisi posisi trading yang diproses.
    """
    if not data or 'data' not in data or 'otherPositionRetList' not in data['data']:
        logging.warning("Invalid data structure received from API.")
        return pd.DataFrame()

    positions = data['data']['otherPositionRetList']
    df = pd.DataFrame(positions)

    # Debugging: Cetak kolom yang tersedia
    logging.info(f"Available columns in DataFrame: {df.columns.tolist()}")

    # Pastikan kolom 'symbol' ada di DataFrame
    if 'symbol' not in df.columns:
        logging.error("Column 'symbol' not found in DataFrame.")
        return pd.DataFrame()

    # Set 'symbol' sebagai index
    df.set_index('symbol', inplace=True)

    # Menghitung estimatedEntrySize
    df['estimatedEntrySize'] = round((abs(df['amount']) / df['leverage']) * df['entryPrice'], 2)

    # Menentukan posisi (LONG/SHORT)
    df['estimatedPosition'] = df['amount'].apply(lambda x: 'LONG' if x > 0 else 'SHORT')

    # Memformat waktu update (UTC+7)
    df['updateTime'] = df['updateTime'].apply(lambda x: datetime.datetime(*x[:-1], x[-1] // 1000))
    df['updateTime'] = df['updateTime'] + timedelta(hours=7)  # Konversi ke UTC+7
    df['updateTime'] = df['updateTime'].dt.strftime('%Y-%m-%d %H:%M:%S')

    # Memilih kolom yang diperlukan
    position_result = df[['estimatedPosition', 'leverage', 'estimatedEntrySize', 
                          'entryPrice', 'markPrice', 'pnl', 'updateTime']]
    return position_result

previous_symbols = {}
previous_position_results = {}
is_first_runs = {uid: True for uid in TARGETED_ACCOUNT_UIDs}

# Function to send new position message
def send_new_position_message(symbol, row, nickname):
    """
    Mengirim pesan Telegram ketika posisi baru dibuka.
    
    Parameters:
        symbol (str): Simbol trading (misalnya, BTCUSDT).
        row (pd.Series): Baris DataFrame yang berisi detail posisi.
        nickname (str): Nickname dari trader.
    """
    estimated_position = row['estimatedPosition']
    leverage = row['leverage']
    estimated_entry_size = row['estimatedEntrySize']
    entry_price = row['entryPrice']
    pnl = row['pnl']
    updatetime = row['updateTime']
    pnl_emoji = "🟢" if pnl >= 0 else "🔴"  # Emoji untuk PnL positif/negatif
    message = (
        f"⚠️ [<b>{nickname}</b>]\n"
        f"❇️ <b>New position opened</b>\n\n"
        f"<b>Position:</b> {symbol} {estimated_position} {leverage}X\n\n"
        f"💵 Base currency - USDT\n"
        f"------------------------------\n"
        f"🎯 <b>Entry Price:</b> {entry_price}\n"
        f"💰 <b>Est. Entry Size:</b> {estimated_entry_size}\n"
        f"{pnl_emoji} <b>PnL:</b> {pnl}\n\n"
        f"🕒 <b>Last Update:</b>\n{updatetime} (UTC+7)\n"
        f"🔗 <a href='{ACCOUNT_INFO_URL}'><b>VIEW PROFILE ON BINANCE</b></a>"
    )
    telegram_send_message(message)

# Function to send closed position message
def send_closed_position_message(symbol, row, nickname):
    """
    Mengirim pesan Telegram ketika posisi ditutup.
    
    Parameters:
        symbol (str): Simbol trading.
        row (pd.Series): Baris DataFrame yang berisi detail posisi.
        nickname (str): Nickname dari trader.
    """
    estimated_position = row['estimatedPosition']
    leverage = row['leverage']
    updatetime = row['updateTime']
    message = (
        f"⚠️ [<b>{nickname}</b>]\n"
        f"⛔️ <b>Position closed</b>\n\n"
        f"<b>Position:</b> {symbol} {estimated_position} {leverage}X\n"
        f"💵 <b>Current Price:</b> {get_markprice(symbol)} USDT\n\n"
        f"🕒 <b>Last Update:</b>\n{updatetime} (UTC+7)\n"
        f"🔗 <a href='{ACCOUNT_INFO_URL}'><b>VIEW PROFILE ON BINANCE</b></a>"
    )
    telegram_send_message(message)

# Function to send current positions
def send_current_positions(position_result, nickname):
    """
    Mengirim pesan Telegram dengan daftar posisi saat ini.
    
    Parameters:
        position_result (pd.DataFrame): DataFrame yang berisi posisi saat ini.
        nickname (str): Nickname dari trader.
    """
    if position_result.empty:
        telegram_send_message(f"⚠️ [<b>{nickname}</b>]\n💎 <b>No positions found</b>")
    else:
        telegram_send_message(f"⚠️ [<b>{nickname}</b>]\n💎 <b>Current positions:</b>")
        for symbol, row in position_result.iterrows():
            estimated_position = row['estimatedPosition']
            leverage = row['leverage']
            estimated_entry_size = row['estimatedEntrySize']
            entry_price = row['entryPrice']
            pnl = row['pnl']
            updatetime = row['updateTime']
            pnl_emoji = "🟢" if pnl >= 0 else "🔴"  # Emoji untuk PnL positif/negatif
            message = (
                f"🔄 <b>Position:</b> {symbol} {estimated_position} {leverage}X\n\n"
                f"💵 Base currency - USDT\n"
                f"------------------------------\n"
                f"🎯 <b>Entry Price:</b> {entry_price}\n"
                f"💰 <b>Est. Entry Size:</b> {estimated_entry_size}\n"
                f"{pnl_emoji} <b>PnL:</b> {pnl}\n\n"
                f"🕒 <b>Last Update:</b>\n{updatetime} (UTC+7)\n"
                f"🔗 <a href='{ACCOUNT_INFO_URL}'><b>VIEW PROFILE ON BINANCE</b></a>"
            )
            telegram_send_message(message)

while True:
    try:
        start_time = time.time()  # Catat waktu mulai iterasi
        
        for TARGETED_ACCOUNT_UID in TARGETED_ACCOUNT_UIDs:
            ACCOUNT_INFO_URL = ACCOUNT_INFO_URL_TEMPLATE.format(TARGETED_ACCOUNT_UID)
            headers = get_header(ACCOUNT_INFO_URL)
            json_data = get_json(TARGETED_ACCOUNT_UID)

            response_nickname = get_nickname(headers, json_data)
            response = get_position(headers, json_data)
            if response is not None and response_nickname is not None:
                nickname_data = json.loads(response_nickname.text)
                if 'data' in nickname_data and 'nickName' in nickname_data['data']:
                    nickname = nickname_data['data']['nickName']
                else:
                    logging.error("Failed to retrieve nickname from API response.")
                    telegram_send_message("Failed to retrieve nickname from API response.")
                    continue

                leaderboard_data = json.loads(response.text)
                position_result = modify_data(leaderboard_data)

                new_symbols = position_result.index.difference(previous_symbols.get(TARGETED_ACCOUNT_UID, pd.Index([])))
                if not is_first_runs[TARGETED_ACCOUNT_UID] and not new_symbols.empty:
                    for symbol in new_symbols:
                        send_new_position_message(symbol, position_result.loc[symbol], nickname)

                closed_symbols = previous_symbols.get(TARGETED_ACCOUNT_UID, pd.Index([])).difference(position_result.index)
                if not is_first_runs[TARGETED_ACCOUNT_UID] and not closed_symbols.empty:
                    for symbol in closed_symbols:
                        if symbol in previous_position_results.get(TARGETED_ACCOUNT_UID, pd.DataFrame()).index:
                            send_closed_position_message(symbol, previous_position_results[TARGETED_ACCOUNT_UID].loc[symbol], nickname)

                if is_first_runs[TARGETED_ACCOUNT_UID]:
                    send_current_positions(position_result, nickname)

                previous_position_results[TARGETED_ACCOUNT_UID] = position_result.copy()
                previous_symbols[TARGETED_ACCOUNT_UID] = position_result.index.copy()
                is_first_runs[TARGETED_ACCOUNT_UID] = False

        # Hitung waktu eksekusi dan log
        ping_time = (time.time() - start_time) * 1000  # Konversi ke milidetik
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"✅ Bot is still running | Time: {current_time} | Ping: {ping_time:.2f}ms")
        
        time.sleep(150)
        
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        message = f"Error occurred for UID <b>{TARGETED_ACCOUNT_UID}</b>:\n{e}\n\n" \
                  f"Retrying after 60s"
        telegram_send_message(message)
        time.sleep(60)
