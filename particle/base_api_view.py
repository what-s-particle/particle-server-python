import logging

from django.http import HttpResponse
from particle.base_particle import BaseParticle

logger = logging.getLogger(__name__)


class BaseHttpResponse(HttpResponse):
    @staticmethod
    def response(request, data: BaseParticle):
        if request.META.get('HTTP_ACCEPT') == 'application/x-protobuf':
            logger.info('application/octet-stream.')
            return HttpResponse(data.pb, content_type='application/octet-stream')
        else:
            logger.info('application/json.')
            return HttpResponse(data.json, content_type='application/json')
