import re
from os import environ
from Script import script 

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
    CACHE_TIME = int(environ.get('CACHE_TIME', 300))
    USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

    PICS = (environ.get('PICS' ,'https://graph.org/file/b1a847cf7ed6752dc335e.jpg https://graph.org/file/104f094ea493183dc65b3.jpg https://graph.org/file/b09e486ebc9e46a7a0d21.jpg https://graph.org/file/2716c5f5494be12585fed.jpg https://graph.org/file/e63188a49ae77fa6847b4.jpg https://graph.org/file/1daa4cef8c914cf930a9f.jpg https://graph.org/file/4403d98e90da5202c7403.jpg https://graph.org/file/1b5ad997c68aa56a42047.jpg https://graph.org/file/fa309f421d35b54ab4916.jpg https://graph.org/file/5c3b48ae914b4a430c699.jpg https://graph.org/file/9597c8bd4931894e0f476.jpg https://graph.org/file/bf25d566ea22bfbe2606b.jpg https://graph.org/file/8a99b7a8b5d1e7d3527eb.jpg https://graph.org/file/d73fbb8a472fc73957b9d.jpg https://graph.org/file/8bbbe9d782ea3588aa6cc.jpg https://graph.org/file/61e89f08fdf8bc31ed391.jpg https://graph.org/file/f1be3ea229b4c2f2b2ba2.jpg https://graph.org/file/304f44482b641a32ff0e0.jpg https://graph.org/file/af1289d41f6213b04356c.jpg https://graph.org/file/858d2dffd191e7bcb5889.jpg https://graph.org/file/32fedd7f8bb9abcb258f2.jpg https://graph.org/file/175490f713ee46dea006e.jpg https://graph.org/file/0d3fb8ce980bcc1476af9.jpg https://graph.org/file/88abb706f3c8c1dc0062e.jpg https://graph.org/file/918f20fea6d752ff9e427.jpg https://graph.org/file/2ae9b9dc10d701ddc0ef7.jpg https://graph.org/file/a8be0175ec7b9f60741f5.jpg https://graph.org/file/566a94549c1667375d6bf.jpg https://graph.org/file/d4d8b6201468e01f5c319.jpg https://graph.org/file/5002dd773f32297d4c716.jpg https://graph.org/file/f5705c9cc5db328d7eb04.jpg https://graph.org/file/bcfa4234fabcc06bbf967.jpg https://graph.org/file/3014886a272bcae1dcfd2.jpg https://graph.org/file/3d0048b649019c0b79930.jpg https://graph.org/file/23e0f601099b3d7240df6.jpg https://graph.org/file/d08ea8b6df5025dff4dd1.jpg https://graph.org/file/f942eed64efc5e15f851f.jpg https://graph.org/file/50e53ba94f56705e62dd2.jpg https://graph.org/file/d024b343c4708a3088e80.jpg https://graph.org/file/83615608530c3b8bce3db.jpg https://graph.org/file/bba41ac784740b921d9a9.jpg https://graph.org/file/ddaa388fcb5ad19ad20da.jpg https://graph.org/file/d018ad53eb91573ca0beb.jpg https://graph.org/file/320842dd97dc5989d8ab7.jpg https://graph.org/file/53e69526140be3632f9b7.jpg https://graph.org/file/dfbbebddf4ca1a2974ac2.jpg https://graph.org/file/7fc7f76632d32e1ef5465.jpg https://graph.org/file/7d716934eddd208ae4a76.jpg https://graph.org/file/e0bf26303935f17295c0d.jpg https://graph.org/file/349cf1684b1f77e781c7f.jpg https://graph.org/file/19fbbd97354334c995b86.jpg https://graph.org/file/a44c903cc292c9806f61a.jpg https://graph.org/file/3819d39bf1939b6feb538.jpg https://graph.org/file/9d7d5abcfdbcf60d13617.jpg https://graph.org/file/e6034e993d6f9c5438339.jpg https://graph.org/file/27f111b5448d45033ee84.jpg https://graph.org/file/f1fc9106eb9d0a57049ab.jpg https://graph.org/file/b71eea0eb720a5f5cfdc5.jpg https://graph.org/file/96be4c9e3601e4b5c701d.jpg https://graph.org/file/789dd1ae557d986453163.jpg https://graph.org/file/9e56def4361543ed85ce6.jpg https://graph.org/file/b3738c06abe86ee467222.jpg https://graph.org/file/0a793188736975fecd61b.jpg https://graph.org/file/a6488015e7d3c0d9f7381.jpg https://graph.org/file/0eecba255304088bce215.jpg https://graph.org/file/9a115b081a159664c9268.jpg https://graph.org/file/17d6f267d2e44aba4f9dc.jpg https://graph.org/file/fe021868b3e13aace5c2e.jpg https://graph.org/file/5a03cc38ec6602951e1a0.jpg https://graph.org/file/f402ff237679bb8eed9f3.jpg https://graph.org/file/1bedbbaa9cd98bf81e886.jpg https://graph.org/file/c612261410ade553ab74b.jpg https://graph.org/file/425003840baac902aca0e.jpg https://graph.org/file/7fae3ae25dd037e5c47a4.jpg https://graph.org/file/86186bb547da26225cee3.jpg https://graph.org/file/2844084bd1e138d4cf2a5.jpg https://graph.org/file/85be9b5a16029f5d27e1e.jpg https://graph.org/file/a44a2c8fd358d96be7dda.jpg https://graph.org/file/2d69b24ccfd7a09ab3920.jpg https://graph.org/file/07708f5b6928b3e327daf.jpg https://graph.org/file/d7a5aa5e569649abaf8d9.jpg https://graph.org/file/b6ee0f5aeb265eb28d439.jpg https://graph.org/file/ec2d8f32df22125b3bfa3.jpg https://graph.org/file/102aded268080cb8b0a2e.jpg https://graph.org/file/8206b270a7ee5c89ae8f1.jpg https://graph.org/file/9d34bdc636a96b803fdc7.jpg https://graph.org/file/5ec31d734e1dfe0683a68.jpg https://graph.org/file/ca87f0995dae8add9a935.jpg https://graph.org/file/b8f8b95db1c2f36eff24b.jpg https://graph.org/file/ca87f0995dae8add9a935.jpg https://graph.org/file/8c2cac7f1f4f39c0ecb81.jpg https://graph.org/file/a64d6d713196341b32d75.jpg https://graph.org/file/9133495f844def6d2daf7.jpg https://graph.org/file/a63f19a58cad0f425c31a.jpg https://graph.org/file/02fe42ed9edbc630f9cd3.jpg https://graph.org/file/0c13f78f69b295737c165.jpg https://graph.org/file/3d8fcd98fb9351562ab35.jpg https://graph.org/file/1688dd1d948ca130c376f.jpg https://graph.org/file/10f52492d25db4227355b.jpg https://graph.org/file/e9991cf25872e8a49ae3a.jpg https://graph.org/file/837f6907b8b7cfcb61e66.jpg https://graph.org/file/6ea067c312a364b0c1cc4.jpg https://graph.org/file/2bd5006ba298bf38e15f0.jpg https://graph.org/file/0f236e7368473be5719f6.jpg https://graph.org/file/1ae43eb114d8ca0305180.jpg https://graph.org/file/34173f015a5fba52f40a2.jpg https://graph.org/file/bae7b77c213009c98ac14.jpg https://graph.org/file/1908b0f8ef6fa74647acc.jpg https://graph.org/file/1c536286ec6af6dd5c8ea.jpg https://graph.org/file/7b71f3f52a24d6ee876ed.jpg https://graph.org/file/fbe7d13c89bbef8446f95.jpg https://graph.org/file/68b43f4f4602ed94eca61.jpg https://graph.org/file/8829bfeb07ca9f8fd25b4.jpg https://graph.org/file/5d47ceec839f76726e2d0.jpg https://graph.org/file/58e96f9f1114bea9f0466.jpg https://graph.org/file/845f61837149d5350563d.jpg https://graph.org/file/92d3c5d18d4382ebb8296.jpg https://graph.org/file/a687c767d49074825344b.jpg https://graph.org/file/fbd387e1330acb02a197d.jpg https://graph.org/file/d4e1284caa8c023a47994.jpg https://graph.org/file/054f4a0a91ebea8f2ca3c.jpg https://graph.org/file/9ab852e8c934fc5ab5498.jpg https://graph.org/file/c694f077bbef367591c53.jpg https://graph.org/file/343af9977b651b2231b0f.jpg https://graph.org/file/c682e7796d9076da0b386.jpg https://graph.org/file/0806a79129be616c9f97e.jpg https://graph.org/file/85898809d4520c19491c8.jpg https://graph.org/file/3a90c7a09450fbb3ef816.jpg https://graph.org/file/71b41235dded336866c28.jpg https://graph.org/file/604788587bc924d1bf64e.jpg https://graph.org/file/dfa43dce2f7b01c6dddd8.jpg https://graph.org/file/0c549ac862c973b7c2cde.jpg https://graph.org/file/684a71b5fffff08452cbc.jpg https://graph.org/file/30c1126ec07f40e4ca8f2.jpg https://graph.org/file/ca45b34d3b92a69c5d0ae.jpg https://graph.org/file/8fa4da125c265d5171a53.jpg https://graph.org/file/8c627bc52a5f951454a35.jpg https://graph.org/file/fa46f9e47bcfcd7e76926.jpg https://graph.org/file/e94d44c334133af51934d.jpg https://graph.org/file/174292d52b7b3afee58d6.jpg https://graph.org/file/a3cf0511972e4f3572acd.jpg https://graph.org/file/1cb3fa8093dc4440c8548.jpg https://graph.org/file/228483251059b644f36c1.jpg https://graph.org/file/9f7b58de726e1f77548ed.jpg https://graph.org/file/046e41aca03d66146b1d2.jpg https://graph.org/file/5fa0b06a8daf5fdfc37af.jpg https://graph.org/file/ece02287c1446d15553be.jpg https://graph.org/file/313b08a645c2b9843b014.jpg https://graph.org/file/43efa38c3f335a3959036.jpg https://graph.org/file/dfae8a9d62bd7cb7dd3fd.jpg https://graph.org/file/53e1d1f10feef0d7e7fe0.jpg https://graph.org/file/24cab4a1540254ae0034f.jpg https://graph.org/file/192836b2c19d934434ab1.jpg https://graph.org/file/1643639d3b23eea1c1bb1.jpg https://graph.org/file/a1d44bc3dd191e4ba82cb.jpg https://graph.org/file/98e7c6a9bd44fe9b00270.jpg https://graph.org/file/ba13f214d07fddf831748.jpg https://graph.org/file/e5a4458b17dac0aba39fd.jpg https://graph.org/file/4baee477b1f7c7d6befe9.jpg https://graph.org/file/64768d736ae7ae7373d92.jpg https://graph.org/file/e75b19361083fbd7240e5.jpg https://graph.org/file/88613154a782c68352921.jpg https://graph.org/file/385b5fbbb26a809930a05.jpg https://graph.org/file/b466f3e1e7884f9609b87.jpg https://graph.org/file/d32a3d597e60e6f08e3ec.jpg https://graph.org/file/d06e713cccca4105d3960.jpg https://graph.org/file/25ba7ca46cbb55cf8d883.jpg https://graph.org/file/20adb3b7cade1eaa3b5df.jpg https://graph.org/file/0d97d7bac7189adc23382.jpg https://graph.org/file/4234f57601d81916bc30d.jpg https://graph.org/file/e34a00ee9cff2aedc6906.jpg https://graph.org/file/36ffed336a6f0a30e0e7b.jpg https://graph.org/file/f1d668fe0a1907ec49d93.jpg https://graph.org/file/2321ae01852db8fd11411.jpg')).split()
    NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/df36d19b8543da0880cf7.jpg")
    MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/6c3ee7bb3e03d07767c3e.mp4")
    SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/df36d19b8543da0880cf7.jpg")

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
    DATABASE_URI = clonedme.DATABASE_URI
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
    SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
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
