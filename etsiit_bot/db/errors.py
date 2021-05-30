# Copyright (c) 2021 Jorge Chamorro Padial, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
"""Common DB errors module."""


class DataBaseError(Exception):
    """Base DB error."""

    pass


class DBUserExistsError(DataBaseError):
    """Raised when a user already exists."""

    pass


class DBUserAlreadySubscribed(DataBaseError):
    """The user is already subscribed."""

    pass
