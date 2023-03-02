from django.http import HttpResponse
from google.protobuf import json_format

from particle.protos import particle_pb2


def index(request):
    modifier = particle_pb2.Modifier(visible=True, clickable=True)
    interactions = []
    component = particle_pb2.TextComponent(content="content")
    element = particle_pb2.ElementComponent(label=component)
    particle = particle_pb2.Particle(id="id-123", element=element, modifier=modifier, interactions=interactions)

    if request.content_type == "application/octet-stream":
        return HttpResponse(particle.SerializeToString(), content_type="application/octet-stream")
    else:
        return HttpResponse(json_format.MessageToJson(particle), content_type="application/json")
