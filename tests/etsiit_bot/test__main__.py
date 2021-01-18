# Copyright (c) 2020 Jorge Chamorro Padial, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
"""Test main entrypoint."""
import unittest

from unittest import TestCase, mock

from etsiit_bot import __main__ as main


class TestMain(TestCase):
    """Test the main entrypoint."""

    @staticmethod
    @mock.patch("etsiit_bot.__main__.run_bot")
    def test_main(mock_run_bot):
        """Test the main function."""
        main.main()
        mock_run_bot.assert_called_once()


if __name__ == "__main__":
    unittest.main()
