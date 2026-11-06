import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API credentials
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Application settings
TIMEZONE = os.getenv("TIMEZONE", "Asia/Kolkata")
NEWS_LIMIT = int(os.getenv("NEWS_LIMIT", "10"))

# Gemini API settings
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

GEMINI_FALLBACK_MODEL = os.getenv("GEMINI_FALLBACK_MODEL")

# Validate required credentials
if not GNEWS_API_KEY:
    raise ValueError("GNEWS_API_KEY is missing in .env")

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is missing in .env")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in .env")

if not GEMINI_MODEL:
    raise ValueError("GEMINI_MODEL is missing in .env")