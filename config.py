import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

OWNER_USERNAME = getenv("OWNER_USERNAME","『sᴀᴛʏᴀᴍ』")
BOT_USERNAME = getenv("BOT_USERNAME" , "@satyam_music_bot")
# ---------------@Mr_majnu72-----------------------------------------
BOT_NAME = getenv("BOT_NAME" , "Satyam_music_bot")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "『sᴀᴛʏᴀᴍ』")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)
#---------------------@mr_majnu72------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ------------------------@mr_majnu72----------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1001919135283))
# --------------------------@mr_majnu72--------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 5097836954))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ChampuXD/SatyamMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
) 
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/satyamnetwork")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/satyambotsupport")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
#| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
#| |     ______   | || |  ____  ____  | || |      __      | || | ____    ____ | || |   ______     | || | _____  _____ | |
#| |   .' ___  |  | || | |_   ||   _| | || |     /  \     | || ||_   \  /   _|| || |  |_   __ \   | || ||_   _||_   _|| |
#| |  / .'   \_|  | || |   | |__| |   | || |    / /\ \    | || |  |   \/   |  | || |    | |__) |  | || |  | |    | |  | |
#| |  | |         | || |   |  __  |   | || |   / ____ \   | || |  | |\  /| |  | || |    |  ___/   | || |  | '    ' |  | |
#| |  \ `.___.'\  | || |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |   _| |_      | || |   \ `--' /   | |
#| |   `._____.'  | || | |____||____| | || ||____|  |____|| || ||_____||_____|| || |  |_____|     | || |    `.__.'    | |
#| |              | || |              | || |              | || |              | || |              | || |              | |
#| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
# '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/8c1f7a6bc105758e4a505.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/2090b4190a472ad3a72b8.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/8b844371e17e292e2e968.jpg"
STATS_IMG_URL = "https://telegra.ph/file/1dd4b0c00f5588e7111de.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/73ec16f7e1abc036cc1d3.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/73ec16f7e1abc036cc1d3.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/664a69066c23e6afc05dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/73ec16f7e1abc036cc1d3.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/73ec16f7e1abc036cc1d3.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d8e61221edba6e9736391.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/ce39a7c4899efd07472d5.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/91ece723994adb8b16bbe.jpg"
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )