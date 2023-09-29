import re
from os import environ
from Script import script 
from info import *
from dotenv import load_dotenv
from typing import Union

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")


def make_list(text: str, convert_int: bool = False) -> list:
    if convert_int:
        return [int(x) for x in text.split()]
    return text.split()


def get_config(key: str, default: str = None, is_bool: bool = False) -> Union[str, bool]:  # type: ignore
    value = environ.get(key)
    if value is None:
        return default
    if is_bool:
        if value.lower() in ["true", "1", "on", "yes"]:
            return True
        elif value.lower() in ["false", "0", "off", "no"]:
            return False
        else:
            raise ValueError
    return value
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class Config:
# Bot settings
    CACHE_TIME = CACHE_TIME
    USE_CAPTION_FILTER = USE_CAPTION_FILTER

    PICS = PICS
    NOR_IMG = NOR_IMG
    MELCOW_VID = MELCOW_VID
    SPELL_IMG = SPELL_IMG

# Admins, Channels & Users
    ADMINS = ADMINS
    CHANNELS = CHANNELS
    AUTH_USERS = AUTH_USERS
    AUTH_CHANNEL = AUTH_CHANNEL
    AUTH_GROUPS = AUTH_GROUPS
    REQST_CHANNEL = REQST_CHANNEL_ID
    SUPPORT_CHAT_ID = SUPPORT_CHAT_ID
    NO_RESULTS_MSG = NO_RESULTS_MSG

# MongoDB information
    DATABASE_URI = DATABASE_URI
    DATABASE_NAME = DATABASE_NAME
    COLLECTION_NAME = COLLECTION_NAME

# Others
    VERIFY = VERIFY
    SHORTLINK_URL = SHORTLINK_URL
    SHORTLINK_API = SHORTLINK_API
    IS_SHORTLINK = IS_SHORTLINK
    DELETE_CHANNELS = DELETE_CHANNELS
    MAX_B_TN = MAX_B_TN
    MAX_BTN = MAX_BTN
    GRP_LNK = GRP_LNK
    CHNL_LNK = CHNL_LNK
    TUTORIAL = TUTORIAL
    IS_TUTORIAL = IS_TUTORIAL
    MSG_ALRT = MSG_ALRT
    LOG_CHANNEL = LOG_CHANNEL
    SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '+r9ArDaaCETE0OGU9')
    P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
    IMDB = is_enabled((environ.get('IMDB', "True")), True)
    AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
    AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
    SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
    CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
    BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
    IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
    LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
    SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
    MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
    INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
    FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
    MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
    PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
    PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

    LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]

    SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]
