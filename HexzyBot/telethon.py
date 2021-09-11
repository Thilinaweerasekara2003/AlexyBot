from telethon import TelegramClient

from HexzyBot.conf import get_int_key, get_str_key

TOKEN = get_str_key("TOKEN", required=True)
NAME = TOKEN.split(":")[0]

tbot = TelegramClient(
    NAME, get_int_key("API_ID", required=True), get_str_key("API_HASH", required=True)
)

# Telethon> V3.0
tbot.start(bot_token=TOKEN)
