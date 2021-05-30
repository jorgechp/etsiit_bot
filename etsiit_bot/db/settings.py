# Copyright (c) 2021 Jorge Chamorro Padial, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
"""Common variables used in the DB module."""
import peewee

DATETIME_FORMAT = "%Y/%m/%d %H:%M"
database_proxy = peewee.Proxy()
