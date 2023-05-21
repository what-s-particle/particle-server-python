from snapshottest.django import SimpleTestCase

import django
import os
import unittest
from particle.particle_component import ParticleWrapper
from showcase.home.first_screen import FirstScreen

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


def api_client_get(url):
    return {
        "url": url,
    }


class TestNavScreen(SimpleTestCase):
    def setUp(self):
        pass

    def test_first_screen(self):
        first_screen = ParticleWrapper(FirstScreen())
        self.assertMatchSnapshot(first_screen.json)

    if __name__ == "__main__":
        unittest.main()
