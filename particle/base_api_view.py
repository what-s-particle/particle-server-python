import logging
from django.http import HttpResponse
from particle.particle_component import ParticleWrapper

logger = logging.getLogger(__name__)


class BaseHttpResponse(HttpResponse):
    @staticmethod
    def response(request, particle_component: ParticleWrapper):
        if request.META.get('HTTP_ACCEPT') == 'application/x-protobuf':
            logger.info('application/octet-stream.')
            return HttpResponse(particle_component.pb, content_type='application/octet-stream')
        else:
            logger.info('application/json.')
            return HttpResponse(particle_component.json, content_type='application/json')
