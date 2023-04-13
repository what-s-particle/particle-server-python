import logging

from particle.base_api_view import BaseHttpResponse
from particle.particle_component import ParticleComponent
from showcase.home.nav_screen import NavScreen

logger = logging.getLogger(__name__)


def index(request):
    logger.info('A GET request was received.')
    nav_graph = ParticleComponent(NavScreen())
    return BaseHttpResponse.response(request, nav_graph)
