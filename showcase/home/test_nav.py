from snapshottest.django import SimpleTestCase

import django
import os
import unittest
from particle.particle_component import ParticleComponent
from showcase.home.first_screen import FirstScreen
from showcase.home.nav_screen import NavScreen

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


def api_client_get(url):
    return {
        "url": url,
    }


class TestHome(SimpleTestCase):
    def setUp(self):
        pass

    def test_nav_screen(self):
        nav_screen = ParticleComponent(NavScreen())
        self.assertMatchSnapshot(nav_screen.json)

    def test_first_screen(self):
        first_screen = ParticleComponent(FirstScreen())
        self.assertMatchSnapshot(first_screen.json)

    if __name__ == "__main__":
        unittest.main()
