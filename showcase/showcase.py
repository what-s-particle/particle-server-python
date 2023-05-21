import logging

from particle.base_api_view import BaseHttpResponse
from particle.particle_component import ParticleWrapper
from showcase.home.first_screen import FirstScreen
from showcase.home.nav_screen import NavScreen
from showcase.home.second_screen import SecondScreen

logger = logging.getLogger(__name__)


def index(request):
    logger.info('A GET request was received.')
    screens = [FirstScreen(), SecondScreen()]
    nav_graph = ParticleWrapper(NavScreen(screens))
    return BaseHttpResponse.response(request, nav_graph)
