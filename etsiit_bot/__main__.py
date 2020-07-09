# Copyright (c) 2020 Jorge Chamorro Padiel, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
"""ETSIIT bot main entrypoint."""
try:
    from etsiit_bot.bot import run_bot
except ModuleNotFoundError:
    from sys import path as syspath
    from pathlib import Path

    syspath.append(str(Path(__file__).parents[1].resolve()))
    from etsiit_bot.bot import run_bot


def main():
    """Start the bot."""
    run_bot()


if __name__ == "__main__":
    main()
