import os, sys, time ; from telethon.sessions import StringSession ; from telethon import TelegramClient ; from var import Var
bot2 = None
UpTime = time.time()
os.system("pip install --upgrade pip")

if Var.STRING_SESSION:
    bot = TelegramClient(StringSession(Var.STRING_SESSION), Var.APP_ID, Var.API_HASH)
else:
    quit(1)
if Var.STRING2:
    bot2 = TelegramClient(StringSession(Var.STRING2), Var.APP_ID, Var.API_HASH)

CMD_LIST = {}
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}
ENV = os.environ.get("ENV", False)

from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
import asyncio

from requests import get
if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=INFO)
    LOGS = getLogger(__name__)
    CONFIG_CHECK = os.environ.get(
        "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

    if CONFIG_CHECK:
        LOGS.info(
            "Please remove the line mentioned in the first hashtag from the config.env file"
        )
        quit(1)
        
    BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
    try:
        BOTLOG_CHATID = int(BOTLOG_CHATID)
    except:
        pass
        
    BOTLOG = sb(os.environ.get("BOTLOG", "True"))
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))
    PM_MESSAGE = os.environ.get(f"PM_MESSAGE", None)
    UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/amitsharma123234/Plus")
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
    DB_URI = os.environ.get("DATABASE_URL", None)
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    AUTONAME_NAME = os.environ.get("AUTONAME_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/usr/bin/chromedriver")
    CHROME_BIN = os.environ.get("CHROME_BIN", "/usr/bin/google_chrome")
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    CUSTOM_AFK = os.environ.get("CUSTOM_AFK", None)
    MASTERS_MSG = os.environ.get("MASTERS_MSG", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", True)
    COUNTRY= str(os.environ.get("COUNTRY", ""))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    AUTOPIC_COMMENT = os.environ.get("AUTOPIC_COMMENT", "")
    AUTOPIC_FONT_COLOUR = os.environ.get("AUTOPIC_FONT_COLOUR", "")
    AUTOPIC_FONT = os.environ.get("AUTOPIC_FONT", "")
    MONGO_URI = os.environ.get("MONGO_URI", "")
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")
else:
    PLACEHOLDER = None

#



# END OF VARS
