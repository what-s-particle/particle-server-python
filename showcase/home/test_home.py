from snapshottest.django import SimpleTestCase

import django
import os
import unittest
from showcase.home.first_screen import FirstScreen
from showcase.home.home import HomeScreen

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


def api_client_get(url):
    return {
        "url": url,
    }


class TestHome(SimpleTestCase):
    def setUp(self):
        pass

    def test_home(self):
        home_json = HomeScreen().json
        self.assertMatchSnapshot(home_json)

    def test_first_screen(self):
        first_screen_json = FirstScreen().json
        self.assertMatchSnapshot(first_screen_json)

    if __name__ == "__main__":
        unittest.main()
