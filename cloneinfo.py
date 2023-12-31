import re
from os import environ
from Script import script 
from pymongo import MongoClient
from pyrogram import Client, filters
from info import *
from dotenv import load_dotenv
from typing import Union
import os
mongo_client = MongoClient(DATABASE_URI)
mongo_db = mongo_client["cloned_bots"]
  
# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

bots = list(mongo_db.bots.find())
for bot in bots:
    bot_token = bot['token']
    ai = Client(
        f"{bot_token}", API_ID, API_HASH,
        bot_token=bot_token,
        plugins={"root": "clone_plugins"},
    )


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
    REQST_CHANNEL = LOG_CHANNEL
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
    SUPPORT_CHAT = SUPPORT_CHAT
    P_TTI_SHOW_OFF = P_TTI_SHOW_OFF
    IMDB = IMDB
    AUTO_FFILTER = AUTO_FFILTER
    AUTO_DELETE = AUTO_DELETE
    SINGLE_BUTTON = SINGLE_BUTTON
    CUSTOM_FILE_CAPTION = CUSTOM_FILE_CAPTION
    BATCH_FILE_CAPTION = BATCH_FILE_CAPTION
    IMDB_TEMPLATE = IMDB_TEMPLATE
    LONG_IMDB_DESCRIPTION = LONG_IMDB_DESCRIPTION
    SPELL_CHECK_REPLY = SPELL_CHECK_REPLY
    MAX_LIST_ELM = MAX_LIST_ELM
    INDEX_REQ_CHANNEL = INDEX_REQ_CHANNEL
    FILE_STORE_CHANNEL = FILE_STORE_CHANNEL
    MELCOW_NEW_USERS = MELCOW_NEW_USERS
    PROTECT_CONTENT = PROTECT_CONTENT
    PUBLIC_FILE_STORE = PUBLIC_FILE_STORE
    LANGUAGES = LANGUAGES
    SEASONS = SEASONS
