from django.http import HttpResponse
from google.protobuf import json_format

from particle.protos.particle import Modifier, TextComponent, ElementComponent, Particle, NavigationComponent, \
    Destination, LayoutComponent


def index(request):
    modifier = Modifier(visible=True, clickable=True)
    interactions = []
    component = TextComponent(content="content")
    element = ElementComponent(label=component)
    destinations = [Particle(id="destination",
                             layout=LayoutComponent(
                                 destination=Destination(
                                     content=Particle(id="text-id", element=element),
                                     route="first"
                                 )
                             )
                             )]

    navigation = NavigationComponent(startDestination="first", destinations=destinations)
    particle = Particle(id="id-123", navigation=navigation, modifier=modifier, interactions=interactions)

    if request.content_type == "application/octet-stream":
        return HttpResponse(particle.SerializeToString(), content_type="application/octet-stream")
    else:
        return HttpResponse(json_format.MessageToJson(particle), content_type="application/json")
