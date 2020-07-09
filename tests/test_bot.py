# Copyright (c) 2020 Jorge Chamorro Padiel, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
"""Test bot module."""
import unittest

from unittest import TestCase, mock

try:
    from etsiit_bot import bot
except ModuleNotFoundError:
    from sys import path as syspath
    from pathlib import Path

    syspath.append(str(Path(__file__).parents[1].resolve()))
    from etsiit_bot import bot


class TestBot(TestCase):
    """Test the bot commands."""

    @staticmethod
    @mock.patch("etsiit_bot.bot.logger")
    def test_log_context(mock_logger):
        """Test the log_context util function."""
        mock_context = mock.Mock()
        mock_context.user_data = {"user_id": 123}
        mock_context.chat_data = {"chat_id": 456}
        bot.log_context(mock_context)

        mock_logger.debug.assert_called_with(
            "Called by %s in %s chat.",
            mock_context.user_data["user_id"],
            mock_context.chat_data["chat_id"],
        )

    @staticmethod
    @mock.patch("etsiit_bot.bot.log_context")
    def test_start(mock_log_context):
        """Test the start function."""
        mock_update = mock.Mock()
        mock_context = mock.Mock()

        bot.start(mock_update, mock_context)

        mock_update.message.reply_text.assert_called_once()
        mock_log_context.assert_called_with(mock_context)

    @staticmethod
    @mock.patch("etsiit_bot.bot.log_context")
    def test_show_help(mock_log_context):
        """Test the show_help function."""
        mock_update = mock.Mock()
        mock_context = mock.Mock()

        bot.show_help(mock_update, mock_context)

        mock_update.message.reply_text.assert_called_once()
        mock_log_context.assert_called_with(mock_context)

    @staticmethod
    @mock.patch("etsiit_bot.bot.log_context")
    def test_echo(mock_log_context):
        """Test the echo function."""
        mock_update = mock.Mock()
        mock_context = mock.Mock()

        bot.echo(mock_update, mock_context)

        mock_update.message.reply_text.assert_called_with(
            mock_update.message.text
        )
        mock_log_context.assert_called_with(mock_context)

    @staticmethod
    @mock.patch("etsiit_bot.bot.logger")
    def test_error(mock_logger):
        """Test the error function."""
        mock_update = mock.Mock()
        mock_context = mock.Mock()

        bot.error(mock_update, mock_context)

        mock_logger.warning.assert_called_with(
            'Update "%s" caused error "%s"', mock_update, mock_context.error
        )

    @mock.patch("etsiit_bot.bot.Updater")
    def test_run_bot(self, mock_updater):
        """Test the bot initialization funtion."""
        bot.CommandHandler = mock.Mock()
        bot.Filters = mock.Mock()
        bot.MessageHandler = mock.Mock()
        bot.run_bot()
        mock_updater_object = mock_updater.return_value

        mock_updater.assert_called_with(
            "TELEGRAM_TOKEN_dummy", use_context=True
        )
        mock_updater_object.start_webhook.assert_called_with(
            listen="0.0.0.0", port=123, url_path="TELEGRAM_TOKEN_dummy"
        )
        mock_updater_object.bot.set_webhook.assert_called_with(
            "https://PROJECT_NAME_dummy.glitch.me/TELEGRAM_TOKEN_dummy"
        )
        mock_dp = mock_updater_object.dispatcher
        self.assertEqual(mock_dp.add_handler.call_count, 3)
        mock_dp.add_error_handler.assert_called_with(bot.error)
        mock_updater_object.idle.assert_called_once()
        self.assertEqual(mock_updater_object, mock_updater())


if __name__ == "__main__":
    unittest.main()
