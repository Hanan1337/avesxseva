import os
import sys
import json
import configparser

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Setup Wizard")

banner()

# Setup Telegram
config_file = 'config.ini'
telegram_info = configparser.RawConfigParser()
telegram_info.add_section('telegram')

xbot = input("[+] Enter Telegram Bot Token: ")
telegram_info.set('telegram', 'bottoken', xbot)

xchat = input("[+] Enter Telegram ChatID: ")
telegram_info.set('telegram', 'chatid', xchat)

with open(config_file, 'w') as setup:
    telegram_info.write(setup)

# Setup UIDs
uids_file = 'uids.json'
uids = []

print("\n[+] Enter Binance UIDs (tekan Enter setelah setiap UID, kosongkan untuk selesai):")
while True:
    uid = input("UID: ").strip()
    if not uid:
        break
    uids.append(uid)

with open(uids_file, 'w') as f:
    json.dump(uids, f, indent=2)

print("\n[+] Setup completed successfully!")
