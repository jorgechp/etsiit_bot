# Copyright (c) 2020 Jorge Chamorro Padial, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
""" Academic related functionalities"""
from typing import Dict

from etsiit.utils import Link


class AcademicInfo:
    """ Information associated to a Degree.

    :ivar Dict [str, Link] teaching_guides: Set of teaching guides.
    :ivar str degree: The degree's name.
    """

    def __init__(self, degree: str) -> None:
        self._degree: str = degree
        self._teaching_guides: Dict[str, Link] = {}

    @property
    def degree(self) -> str:
        """ The degree's name.

        :return: The degree's name.
        """
        return self._degree

    @property
    def teaching_guides(self) -> Dict[str, Link]:
        """ Degree's Teaching guides.

        :return: The Degree's Teaching guides.
        """
        return self._teaching_guides

    def add_teaching_guide(self, teaching_guide: Link) -> None:
        """ Add a new teaching guide.

        .. note::
            This method will override any existing teaching guide.

        :param teaching_guide: The new teaching guide.
        """

        self._teaching_guides[teaching_guide.name] = teaching_guide
