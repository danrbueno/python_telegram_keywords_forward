# This python project watches new messages in Telegram groups that a user is included.
# And then forward the messages to a specific group based on a list of keywords.
# 1. Get all the Telegram groups/channels where's my user is added
# 2. Get new messages based on keywords list from these groups/channels
# 3. Forward them to a specific group/channel
# 4. This group/channel has a bot that receives the message and then send it to the logged user

from telethon import TelegramClient, sync, events
from telethon.sessions import StringSession
import telebot
from os import getenv

def get_keywords(file):
    keywords_list = []

    with open(file=file, mode='r') as keywords_file:
        for line in keywords_file:
            keyword = line.strip()
            keywords_list.append(keyword)
    
    return keywords_list

def get_peer_messages():
    bot_api_hash = getenv("TELEGRAM_BOT_API_HASH")
    recipient = int(getenv("TELEGRAM_RECIPIENT_ID"))
    api_string = getenv("TELEGRAM_API_STRING")
    api_id = int(getenv("TELEGRAM_API_ID"))
    api_hash = getenv("TELEGRAM_API_HASH")

    keywords_list = get_keywords("keywords.txt")

    with open(file="keywords.txt", mode='r', newline="\n") as keywords_file:
        for line in keywords_file:
            keyword = line.strip()
            keywords_list.append(keyword)

    client = TelegramClient(StringSession(api_string), api_id, api_hash)
    client.start()
    
    bot = telebot.TeleBot(bot_api_hash)

    me = client.get_me()
    my_user_id = me.id

    all_chats = client.get_dialogs()
    chat_list = [
        chat
        for chat in all_chats
        if (chat.is_user==False) and (chat.id != recipient)
    ]

    @client.on(events.NewMessage(chats=[chat.id for chat in chat_list]))
    async def get_new_message(event):
        message = event.message
        message_text = message.raw_text

        for key_word in keywords_list:
            if key_word.lower() in message_text.lower():
                await client.forward_messages(
                    entity=recipient, messages=[message.id], from_peer=message.peer_id
                )

                async for last_message in client.iter_messages(
                    entity=recipient, limit=1
                ):
                    bot.forward_messages(
                        chat_id=my_user_id,
                        from_chat_id=recipient,
                        message_ids=[last_message.id],
                    )
                break

    client.run_until_disconnected()

if __name__ == "__main__":
    get_peer_messages()