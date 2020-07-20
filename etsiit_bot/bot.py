# Copyright (c) 2020 Jorge Chamorro Padiel, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
"""Bot initializer and methods."""
import logging

from telegram import Update  # type: ignore
from telegram.ext import (  # type: ignore
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    Updater,
)

from etsiit_bot.settings import PORT, PROJECT_NAME, TELEGRAM_TOKEN

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update
# and context. Error handlers also receive the raised TelegramError object in
# error.
def log_context(context: CallbackContext) -> None:
    """Log every message handled."""
    logger.debug(
        "Called by %s in %s chat.",
        context.user_data["user_id"],
        context.chat_data["chat_id"],
    )


def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hi!")
    log_context(context)


def show_help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Help!")
    log_context(context)


def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    log_context(context)


def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def run_bot():
    """Initialize and run bot."""
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TELEGRAM_TOKEN)

    updater.bot.set_webhook(
        f"https://{PROJECT_NAME}.glitch.me/{TELEGRAM_TOKEN}"
    )

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", show_help))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dispatcher.add_error_handler(error)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
