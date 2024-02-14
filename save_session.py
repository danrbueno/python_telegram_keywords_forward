from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from os import getenv

api_id = int(getenv("TELEGRAM_API_ID"))
api_hash = getenv("TELEGRAM_API_HASH")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())