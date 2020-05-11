from decouple import config

TELEGRAM_TOKEN = config("TELEGRAM_TOKEN", cast=str)
PROJECT_NAME = config("PROJECT_NAME", default="ETSIIT-bot", cast=str)
