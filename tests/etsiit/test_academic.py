# Copyright (c) 2021 Jorge Chamorro Padial, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
"""ETSIIT academic testing module."""

from unittest import TestCase

from etsiit.academic import AcademicInfo
from etsiit.utils import Link


class TestAcademic(TestCase):
    """Test the Academic class."""

    def test_init(self):
        """Test the class constructor."""
        degree = "link-name"

        academic = AcademicInfo(degree)

        self.assertEqual(degree, academic.degree)
        self.assertFalse(academic.teaching_guides)

    def test_add_teaching_guide(self):
        """Test the teaching guide addition."""

        degree = "link-name"

        mock_name = "link-name"
        mock_url = "link-url"

        test_link = Link(mock_name, mock_url)

        academic = AcademicInfo(degree)
        academic.add_teaching_guide(test_link)

        self.assertDictEqual(
            academic.teaching_guides, {test_link.name: test_link}
        )
