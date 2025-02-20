import requests
import time
from message import telegram_send_message

def get_position(headers, json_data, max_retries=5):
    """
    Mendapatkan posisi trading dari Binance Futures Leaderboard menggunakan API terbaru.
    
    Parameters:
        headers (dict): Header yang diperlukan untuk request HTTP.
        json_data (dict): Payload yang dikirim sebagai body request.
        max_retries (int): Jumlah maksimum percobaan ulang jika terjadi kesalahan koneksi.
    
    Returns:
        requests.Response: Respons dari API.
    """
    url = "https://www.binance.com/bapi/futures/v2/private/future/leaderboard/getOtherPosition"
    retry_count = 0

    while retry_count <= max_retries:
        try:
            response = requests.post(url, headers=headers, json=json_data)
            if response.status_code == 200:
                return response
            else:
                print(f"API request failed with status code: {response.status_code}")
                telegram_send_message(f"API request failed with status code: {response.status_code}")
                raise requests.exceptions.RequestException(f"Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Connection error occurred: {e}")
            telegram_send_message(f"Connection error occurred: {e}")
            if retry_count >= max_retries:
                telegram_send_message("Max retry count reached. Waiting for 10 minutes before next try...")
                time.sleep(600)
                retry_count = 0
            else:
                print("Retrying in 5 seconds...")
                time.sleep(5)
                retry_count += 1
    return None

def get_nickname(headers, json_data, max_retries=5):
    """
    Mendapatkan informasi dasar (seperti nickname) dari trader di Binance Futures Leaderboard menggunakan API terbaru.
    
    Parameters:
        headers (dict): Header yang diperlukan untuk request HTTP.
        json_data (dict): Payload yang dikirim sebagai body request.
        max_retries (int): Jumlah maksimum percobaan ulang jika terjadi kesalahan koneksi.
    
    Returns:
        requests.Response: Respons dari API.
    """
    url = "https://www.binance.com/bapi/futures/v2/public/future/leaderboard/getOtherLeaderboardBaseInfo"
    retry_count = 0

    while retry_count <= max_retries:
        try:
            response = requests.post(url, headers=headers, json=json_data)
            if response.status_code == 200:
                return response
            else:
                print(f"API request failed with status code: {response.status_code}")
                telegram_send_message(f"API request failed with status code: {response.status_code}")
                raise requests.exceptions.RequestException(f"Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Connection error occurred: {e}")
            telegram_send_message(f"Connection error occurred: {e}")
            if retry_count >= max_retries:
                telegram_send_message("Max retry count reached. Waiting for 10 minutes before next try...")
                time.sleep(600)
                retry_count = 0
            else:
                print("Retrying in 5 seconds...")
                time.sleep(5)
                retry_count += 1
    return None

def get_markprice(symbol):
    """
    Mendapatkan harga mark (mark price) dari Binance Futures API.
    
    :param symbol: Simbol trading (misalnya, BTCUSDT).
    :return: Harga mark atau pesan kesalahan jika gagal.
    """
    api_url = "https://fapi.binance.com/fapi/v1/premiumIndex"
    req_data = requests.get(api_url, params={"symbol": symbol})
    try:
        data = req_data.json()
        return data['markPrice']
    except Exception:
        return "Market price retrieval error"
