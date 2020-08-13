from userbot import bot
from sys import argv
import sys
from var import boss as lukkhha
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot import LOAD_PLUG, BOTLOG_CHATID, LOGS, PLUG
from pathlib import Path
import asyncio
import telethon.utils
from telethon import events, functions, types
from telethon.tl.types import InputMessagesFilterDocument
import traceback
kamina = lukkhha
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Plus+ UserBot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()
    

async def a():
    username = kamina
    plug = await bot.get_messages(username, None , filter=InputMessagesFilterDocument) ; total = int(plug.total) ; total_doxx = range(0, total)
    for ixo in total_doxx:
        mxo = plug[ixo].id ; await bot.download_media(await bot.get_messages(username, ids=mxo), "userbot/")
bot.loop.run_until_complete(a())

os.system("mkdir /root/userbot/fonts && cd /root/userbot/fonts && gdown https://drive.google.com/uc?id=1LkOm6318PNStv_eHfCsfD4Jfyj31GVVj&export=download")

import userbot._core

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()


