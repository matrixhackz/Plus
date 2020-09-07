import os
from pymongo import MongoClient
import pymongo
Config = Var

class Var(object):
    LOGGER = True
    APP_ID = int(os.environ.get("APP_ID", None))
    API_HASH = os.environ.get("API_HASH", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    STRING2 = os.environ.get("STRING2", None)
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID", None)
    if PRIVATE_GROUP_BOT_API_ID:
        PRIVATE_GROUP_BOT_API_ID = int(PRIVATE_GROUP_BOT_API_ID)
    PRIVATE_CHANNEL_BOT_API_ID = os.environ.get("PRIVATE_CHANNEL_BOT_API_ID", None)
    if PRIVATE_CHANNEL_BOT_API_ID:
        PRIVATE_CHANNEL_BOT_API_ID = int(PRIVATE_CHANNEL_BOT_API_ID)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./userbot/DOWNLOADS/")
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    HASH_TO_TORRENT_API = os.environ.get("HASH_TO_TORRENT_API", "https://example.com/torrent/{}");
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "mrconfused")
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    G_BAN_LOGGER_GROUP = os.environ.get("BOTLOG_CHATID", None)
    if G_BAN_LOGGER_GROUP:
        G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)
    TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    NO_LOG_P_M_S = bool(os.environ.get("NO_LOG_P_M_S", False))
    MAX_MESSAGE_SIZE_LIMIT = 4095
    UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split())
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(os.environ.get("NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD", 5))
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "\.")
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
    VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    TELE_GRAM_2FA_CODE = os.environ.get("TELE_GRAM_2FA_CODE", None)
    GROUP_REG_SED_EX_BOT_S = os.environ.get("GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot")
    OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", "0")
    OPEN_LOAD_KEY = os.environ.get("OPEN_LOAD_KEY", "0")
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO",None)
    SPOTIFY_BIO_PREFIX = os.environ.get("SPOTIFY_BIO_PREFIX",None)
    SPOTIFY_PASS = os.environ.get("SPOTIFY_PASS",None)
    SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME",None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    DEFAULT_NAME = os.environ.get("DEFAULT_NAME",None)
    VIRUSTOTAL_API_KEY = os.environ.get("VIRUSTOTAL_API_KEY", None)
    AUTONAME_NAME = os.environ.get("AUTONAME_NAME", None)
    CUSTOM_AFK = os.environ.get("CUSTOM_AFK", None)
    MASTERS_MSG = os.environ.get("MASTERS_MSG", None)
    COUNTRY= str(os.environ.get("COUNTRY", ""))
    AUTOPIC_COMMENT = os.environ.get("AUTOPIC_COMMENT", "")
    MAX_FLOOD_IN_P_M_s = os.environ.get("MAX_FLOOD_IN_P_M_s", None)
    MONGO_URI = os.environ.get("MONGO_URI", None)
    PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID", None)
    if PM_LOGGR_BOT_API_ID:
        PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
    TL_VID_STREAM_TYPES = ("MKV", "MP4", "WEBM")
    TL_MUS_STREAM_TYPES = ("MP3", "WAV", "FLAC")
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    ANTI_SPAMBOT = os.environ.get("ANTI_SPAMBOT", None)
    ANTI_SPAMBOT_SHOUT = os.environ.get("ANTI_SPAMBOT_SHOUT", None)
    API_TOKEN = os.environ.get("API_TOKEN",None)
    BOTLOG = os.environ.get("BOTLOG", True)
    PM_LOGGR_BOT_API_ID = int(os.environ.get("PM_LOGGR_BOT_API_ID", "-100"))
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None)
    GENIUS = os.environ.get("GENIUS", None)
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", None))
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    HASH_TO_TORRENT_API = os.environ.get("HASH_TO_TORRENT_API", "https://example.com/torrent/{}");
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split())
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    if AUTH_TOKEN_DATA != None:
        if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
            os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY+"auth_token.txt","w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    CHROME_BIN = os.environ.get("CHROME_BIN", None)
    UPSTREAM_REPO_URL = os.environ.get("UPSTREAM_REPO_URL", "https://github.com/amitsharma123234/Plus.git")
MONGOCLIENT = MongoClient(Var.MONGO_URI, 27017, serverSelectionTimeoutMS=1)
MONGO = MONGOCLIENT.userbot


def is_mongo_alive():
    try:
        MONGOCLIENT.server_info()
    except BaseException:
        return False
    return True





class Production(Var):
    LOGGER = False


class Development(Var):
    LOGGER = True
