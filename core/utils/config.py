import logging
from os import getenv

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = getenv("BOT_TOKEN")
ALERTS_TOKEN = getenv("ALERTS_TOKEN")
DORM_CHAT_ID = getenv("DORM_CHAT_ID")
WEBHOOK_SECRET = getenv("WEBHOOK_SECRET")
BASE_WEBHOOK_URL = getenv("BASE_WEBHOOK_URL")
WEB_SERVER_HOST = getenv("WEB_SERVER_HOST")
WEB_SERVER_PORT = int(getenv("WEB_SERVER_PORT"))
TEST_CHAT_ID = getenv("TEST_CHAT_ID")
ADMIN_ID = getenv("ADMIN_ID")
OWM_API = getenv("OWM_API")

# Create a list of ADMIN_IDS from a .env file
if ADMIN_ID:
    ADMIN_IDS = list(map(int, ADMIN_ID.split(", ")))
else:
    logging.exception("Check your .env file. There is something wrong with ADMIN_ID")
