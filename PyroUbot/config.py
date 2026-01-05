import os
from dotenv import load_dotenv

load_dotenv(".env")
MAX_BOT = int(os.getenv("MAX_BOT", "100"))
DEVS = list(map(int, os.getenv("DEVS", "6918729990").split()))
API_ID = int(os.getenv("API_ID", "27979177"))
API_HASH = os.getenv("API_HASH", "9d3fc5f71dfa8b070c716868f709cb32")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8502900943:AAFd-uphNwQQWlY-A-Tkar_PqHQdejyxnH8")
OWNER_ID = int(os.getenv("OWNER_ID", "6918729990"))
BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763").split()))
RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ibnumuzakim7:ibnumuzakim132@ibnumuzakim.sbwnig8.mongodb.net/")
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4912568273"))
