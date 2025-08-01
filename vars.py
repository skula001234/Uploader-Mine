#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22422690"))
API_HASH = environ.get("API_HASH", "2884fbc53b44a1bbcfa7c525e185c1aa")
BOT_TOKEN = environ.get("BOT_TOKEN", "Dᴇᴠ Tʜᴀɴᴏꜱ")

OWNER = int(environ.get("OWNER", "7793257011"))
CREDIT = environ.get("CREDIT", "@MrFrontMan001")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5680454765').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

# अपनी IMAGE URLs यहां सेट करें:
FEATURE_IMAGE = environ.get(
    "FEATURE_IMAGE",
    "https://envs.sh/S91.jpg/IMG20250728115.jpg"
)

START_IMAGE = environ.get(
    "START_IMAGE",
    "https://envs.sh/S9U.jpg/IMG20250728459.jpg"
)

#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
