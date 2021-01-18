# Copyright (c) 2020 Jorge Chamorro Padial, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
"""Common project settings."""
from pathlib import Path

from decouple import config  # type: ignore

REPO_ROOT = Path(__file__).resolve().parents[1]
TELEGRAM_TOKEN = config("TELEGRAM_TOKEN", cast=str)
PROJECT_NAME = config("PROJECT_NAME", default="ETSIIT-bot", cast=str)
PORT = config("PORT", default="8443", cast=int)
