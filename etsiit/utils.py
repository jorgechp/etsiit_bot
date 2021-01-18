# Copyright (c) 2020 Jorge Chamorro Padial, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
"""Utils functionalities."""


class Link:
    """Simple link information.

    :ivar str _name: name of the Link.
    :ivar str _url: url of the Link.
    """

    def __init__(self, name: str, url: str) -> None:
        """Class constructor.

        :param name: link name.
        :param url: link url.
        """
        self._name = name
        self._url = url

    @property
    def name(self) -> str:
        """The link's name.
        :return: The link's name.
        """
        return self._name

    @property
    def url(self) -> str:
        """The link's url.
        :return: The link's url.
        """
        return self._url

    def to_markdown(self) -> str:
        """Convert the Link to Markdown format."""
        return f"[{self._name}]({self._url})"

    def __str__(self) -> str:
        """To string method."""
        return f"{self._name}: {self._url}"

    def __repr__(self) -> str:
        """Link representation string."""
        return str(self)
