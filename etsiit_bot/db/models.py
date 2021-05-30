# Copyright (c) 2020 Jorge Chamorro Padial, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
"""Data Base model definition."""

import peewee

from etsiit_bot.db.settings import database_proxy, DATETIME_FORMAT


class BaseModel(peewee.Model):
    """Data base class."""

    class Meta:
        """Meta class for the database."""

        database = database_proxy


class User(BaseModel):
    """Model to define users in the database"""

    id: peewee.BigIntegerField = peewee.BigIntegerField(primary_key=True)
    sub_canteen_menu: peewee.BooleanField = peewee.BooleanField()
    active: peewee.BooleanField = peewee.BooleanField()

    class Meta:
        """ Meta class for User."""

        table_name = "USER"


class MeetUp(BaseModel):
    """Model to define MeetUp updates in the database"""

    group_name: peewee.CharField = peewee.CharField(primary_key=True)
    last_update: peewee.DateTimeField = peewee.DateTimeField(
        formats=DATETIME_FORMAT, null=False
    )

    class Meta:
        """ Meta class for MeetUp updates."""

        table_name = "MEETUP"


class MeetUpUser(BaseModel):
    """Model to define MeetUp user subscriptions in the database"""

    group_name: peewee.ForeignKeyField = peewee.ForeignKeyField(
        MeetUp, on_delete="CASCADE"
    )
    user_id: peewee.ForeignKeyField = peewee.ForeignKeyField(
        User, on_delete="CASCADE"
    )

    class Meta:
        """ Meta class for MeetUpUser."""

        primary_key = peewee.CompositeKey("group_name", "user_id")
        table_name = "MEETUP_USER"


class RSS(BaseModel):
    """Model to define RSS in the database"""

    name: peewee.CharField = peewee.CharField(primary_key=True)
    url: peewee.CharField = peewee.CharField(null=False)
    last_update: peewee.DateTimeField = peewee.DateTimeField(
        formats=DATETIME_FORMAT, null=False
    )

    class Meta:
        """ Meta class for RSS."""

        table_name = "RSS"


class RSSUser(BaseModel):
    """Model to define RSS user subscriptions in the database"""

    name: peewee.ForeignKeyField = peewee.ForeignKeyField(
        RSS, on_delete="CASCADE"
    )
    user_id: peewee.ForeignKeyField = peewee.ForeignKeyField(
        User, on_delete="CASCADE"
    )

    class Meta:
        """ Meta class for RSSUser."""

        primary_key = peewee.CompositeKey("name", "user_id")
        table_name = "RSS_USER"
