import logging

from particle.base_api_view import ParticleHttpResponse
from showcase.home.home import HomeScreen

logger = logging.getLogger(__name__)


def get(request):
    logger.info('A GET request was received.')
    nav_graph = HomeScreen.render()
    return ParticleHttpResponse.response(request, nav_graph)
