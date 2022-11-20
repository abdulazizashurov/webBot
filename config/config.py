import os

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CLICK_TOKEN = os.getenv("CLICK_TOKEN")
URL = os.getenv("URL")