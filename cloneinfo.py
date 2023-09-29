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
    ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
    CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
    auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
    AUTH_USERS = (auth_users + ADMINS) if auth_users else []
    PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
    auth_channel = environ.get('AUTH_CHANNEL')
    auth_grp = environ.get('AUTH_GROUP')
    AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
    AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
    support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
    reqst_channel = environ.get('REQST_CHANNEL_ID', '')
    REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
    SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
    NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
    DATABASE_URI = DATABASE_URI
    DATABASE_NAME = environ.get('DATABASE_NAME', "")
    COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
    VERIFY = bool(environ.get('VERIFY', False))
    SHORTLINK_URL = environ.get('SHORTLINK_URL', 'mplaylink.com')
    SHORTLINK_API = environ.get('SHORTLINK_API', '1f1da5c9df9a58058w672acw8d8134e203b03426a1')
    SECOND_SHORTLINK_URL = environ.get('SECOND_SHORTLINK_URL', 'mplaylink.com')
    SECOND_SHORTLINK_API = environ.get('SECOND_SHORTLINK_API', '1f1da5c9df9a58058672a3c8ed8134e203b03426a1')
    IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
    DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
    MAX_B_TN = environ.get("MAX_B_TN", "5")
    MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
    PORT = environ.get("PORT", "8080")
    GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+ps2An00KwZYwNTRl')
    CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/TeamHMT_Bots')
    TUTORIAL = environ.get('TUTORIAL', 'https://t.me/Team_HMT/8')
    IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
    MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
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
