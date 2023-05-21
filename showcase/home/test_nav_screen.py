from snapshottest.django import SimpleTestCase

import django
import os
import unittest
from particle.particle_component import ParticleWrapper
from particle.protos.particle import Particle
from showcase.home.nav_screen import NavScreen

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


def api_client_get(url):
    return {
        "url": url,
    }


class TestNavScreen(SimpleTestCase):
    def setUp(self):
        pass

    def test_nav_screen(self):
        screens = [ParticleWrapper(Particle()).data, ParticleWrapper(Particle()).data]
        nav_screen = ParticleWrapper(NavScreen(screens))
        self.assertMatchSnapshot(nav_screen.json)

    if __name__ == "__main__":
        unittest.main()
