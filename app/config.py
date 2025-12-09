# app/config.py
from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env into environment

COHERE_API_KEY = os.getenv("COHERE_API_KEY", "")
COHERE_MODEL = os.getenv("COHERE_MODEL", "command-mini")
COHERE_MAX_TOKENS = int(os.getenv("COHERE_MAX_TOKENS", "120"))
COHERE_TEMPERATURE = float(os.getenv("COHERE_TEMPERATURE", "0.3"))

APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", "8000"))
APP_DEBUG = os.getenv("APP_DEBUG", "true").lower() in ("1", "true", "yes")
