from django.http import HttpResponse
from google.protobuf import json_format

from particle.protos.particle import Modifier, TextComponent, ElementComponent, Particle


def index(request):
    modifier = Modifier(visible=True, clickable=True)
    interactions = []
    component = TextComponent(content="content")
    element = ElementComponent(label=component)
    particle = Particle(id="id-123", element=element, modifier=modifier, interactions=interactions)

    if request.content_type == "application/octet-stream":
        return HttpResponse(particle.SerializeToString(), content_type="application/octet-stream")
    else:
        return HttpResponse(json_format.MessageToJson(particle), content_type="application/json")
