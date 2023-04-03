import logging

from django.http import HttpResponse
from google.protobuf.json_format import MessageToJson

logger = logging.getLogger(__name__)


class ParticleHttpResponse(HttpResponse):
    @staticmethod
    def response(request, data):
        if request.META.get('HTTP_ACCEPT') == 'application/x-protobuf':
            logger.info('application/octet-stream.')
            return HttpResponse(data.SerializeToString(), content_type='application/octet-stream')
        else:
            logger.info('application/json.')
            return HttpResponse(MessageToJson(data), content_type='application/json')
