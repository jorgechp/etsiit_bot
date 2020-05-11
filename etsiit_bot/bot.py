import telebot
from os import environ
from etsiit_bot.settings import PROJECT_NAME, TELEGRAM_TOKEN

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot_text = (
        "Howdy, how are you doing? Source code on "
        f"https://glitch.com/~{PROJECT_NAME}"
    )
    bot.reply_to(message, bot_text)

bot.set_webhook(f"https://{PROJECT_NAME}.glitch.me/{TELEGRAM_TOKEN}")
