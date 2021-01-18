# Copyright (c) 2021 Jorge Chamorro Padial, Luis Liñán Villafranca. All rights
# reserved.
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>
"""ETSIIT utils testing module."""

from unittest import TestCase

from etsiit.utils import Link


class TestLink(TestCase):
    """Test the Link class."""

    def test_init(self):
        """Test the class constructor."""
        mock_name = "link-name"
        mock_url = "link-url"

        link = Link(mock_name, mock_url)

        self.assertEqual(mock_name, link.name)
        self.assertEqual(mock_url, link.url)

    def test_representations(self):
        """Test the class conversion."""
        mock_name = "link-name"
        mock_url = "link-url"

        link = Link(mock_name, mock_url)

        self.assertEqual(str(link), f"{mock_name}: {mock_url}")
        self.assertEqual(repr(link), f"{mock_name}: {mock_url}")
        self.assertEqual(link.to_markdown(), f"[{mock_name}]({mock_url})")
