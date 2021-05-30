# Copyright (c) 2021 Jorge Chamorro Padial, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
"""Data Base ORM class definition."""

from typing import List
from datetime import datetime

import peewee

from etsiit_bot.models import (
    database_proxy,
    MeetUp,
    MeetUpUser,
    User,
    RSS,
    RSSUser,
)
from etsiit_bot.errors import DBUserExistsError, DBUserAlreadySubscribed


class DBManager:
    """Main entrypoint for the DataBase.

    :ivar database_proxy: database cursor.

    """

    def __init__(self, database: peewee.Database) -> None:
        """Initialises the DB."""
        database_proxy.initialize(database)

    def open(self) -> None:
        """Opens a connection to the database."""
        database_proxy.connect()

    def close(self) -> None:
        """Closes the database connection."""
        database_proxy.close()

    def add_user(self, user_id: int) -> bool:
        """Create a new user.

        :param user_id: user id.
        :returns: whether the creation went ok.
        :raises DBUserExistsError: if the user already exists in the DB.

        """
        try:
            insertion = User.create(
                id=user_id, sub_canteen_menu=False, active=True
            )
        except peewee.IntegrityError as error:
            raise DBUserExistsError(
                "User already exists in the data base"
            ) from error

        return insertion.user_id == user_id

    def delete_user(self, user_id: int) -> bool:
        """Deletes a user.

        :param user_id: user id.
        :returns: whether the insertion went ok.

        """
        return User.delete().where(User.id == user_id).execute() != 0

    def is_user_active(self, user_id: int) -> bool:
        """Checks if an user is active.

        :param user_id: user id.
        :returns: true if the user is active.

        """
        return User.select(User.active).where(User.id == user_id).active

    def set_user_active(self, user_id: int, active: bool) -> bool:
        """Defines the active state of the user.

        :param user_id: user id.
        :param active: the new state of the user.
        :returns: whether the update went ok.

        """
        return (
            User.update(active=active).where(User.id == user_id).execute() != 0
        )

    def is_user_subscribed_canteen_menu(self, user_id: int) -> bool:
        """Checks if an user is subscribed to the canteen menu.

        :param user_id: user id.
        :returns: true if the user is subscribed to the canteen menu.

        """
        return (
            User.select(User.sub_canteen_menu)
            .where(User.id == user_id)
            .sub_canteen_menu
        )

    def set_user_subscribed_canteen_menu(
        self, user_id: int, subscribed: bool
    ) -> bool:
        """Defines the subscription state of the user.

        :param user_id: user id.
        :subscribed: the new state of the subscription.
        :returns: whether the update went ok.

        """
        return (
            User.update(sub_canteen_menu=subscribed)
            .where(User.id == user_id)
            .execute()
            != 0
        )

    def get_user_meetups(self, user_id: int) -> List[str]:
        """Obtain the groups to which the user is subscribed.

        :param user_id: user id.
        :returns: the user MeetUps.

        """
        return MeetUpUser.select(MeetUpUser.group_name).where(
            MeetUpUser.user_id == user_id
        )

    def subscribe_user_meetup(self, user_id: int, group_name: str) -> bool:
        """Subscribes an user to a new MeetUp group.

        :param user_id: user id.
        :param group_name: name of the MeetUp group.
        :returns: true if the insertion went ok.

        """
        if (
            not MeetUp.select(MeetUp.group_name)
            .where(MeetUp.group_name == group_name)
            .count()
        ):
            MeetUp.create(group_name=group_name, last_update=datetime.now())

        try:

            insertion = MeetUpUser.create(
                group_name=group_name, user_id=user_id
            )
        except peewee.IntegrityError as error:
            raise DBUserAlreadySubscribed(
                "User is already subscribed to the MeetUp group"
            ) from error

        return (
            insertion.user_id == user_id and insertion.group_name == group_name
        )

    def unsubscribe_user_meetup(self, user_id: int, group_name: str) -> bool:
        """Unsubscribes an user from a meetup group.

        :param user_id: user id.
        :param group_name: name of the MeetUp group.
        :returns: whether the deletion went ok.

        """
        return (
            MeetUpUser.delete()
            .where(
                MeetUpUser.user_id == user_id
                and MeetUpUser.group_name == group_name
            )
            .execute()
            != 0
        )

    def get_meetup_users(self, group_name: str) -> List[int]:
        """Obtains the users subscribed to a MeetUp group.

        :param group_name: name of the MeetUp group.
        :returns: a list of users subscribed to the group.

        """
        return MeetUpUser.select(MeetUpUser.user_id).where(
            MeetUpUser.group_name == group_name
        )

    def get_user_rss(self, user_id: int) -> List[str]:
        """Obtain the RSSs to which the user is subscribed.

        :param user_id: user id.
        :returns: the user RSSs.

        """
        return RSSUser.select(RSSUser.name).where(RSSUser.user_id == user_id)

    def subscribe_user_rss(self, user_id: int, name: str, url: str) -> bool:
        """Subscribes an user to a new RSS.

        :param user_id: user id.
        :param name: name of the RSS.
        :param url: URL of the RSS.
        :returns: true if the insertion went ok.

        """
        if not RSS.select(RSS.name).where(RSS.name == name).count():
            RSS.create(name=name, url=url, last_update=datetime.now())

        try:
            insertion = RSSUser.create(name=name, user_id=user_id)
        except peewee.IntegrityError as error:
            raise DBUserAlreadySubscribed(
                "User is already subscribed to the RSS"
            ) from error

        return insertion.user_id == user_id and insertion.name == name

    def unsubscribe_user_rss(self, user_id: int, name: str) -> bool:
        """Unsubscribes an user from a meetup group.

        :param user_id: user id.
        :param name: name of the RSS.
        :returns: whether the deletion went ok.

        """
        return (
            RSSUser.delete()
            .where(RSSUser.user_id == user_id and RSSUser.name == name)
            .execute()
            != 0
        )

    def get_rss_users(self, name: str) -> List[str]:
        """Obtains the users subscribed to a RSS.

        :param name: name of the RSS.
        :returns: a list of users subscribed to the RSS.

        """
        return RSSUser.select(RSSUser.user_id).where(RSSUser.name == name)
