from django.http import HttpResponse
from google.protobuf import json_format

from particle.protos.particle import Modifier, TextComponent, Particle, \
    BottomBarComponent, BottomBarItemComponent, TopBarComponent, ScreenComponent, NavGraphComponent, \
    ModalDrawerComponent, DEFAULT_ARROW_BACK


def index(request):
    modifier = Modifier(visible=True, clickable=True)
    interactions = []

    screens = [screen1(), screen2()]

    nav_graph = Particle(
        id="nav_graph",
        interactions=interactions,
        modifier=modifier,
        navGraph=NavGraphComponent(startDestination="screen1", screens=screens))

    if request.META.get('HTTP_ACCEPT') == 'application/x-protobuf':
        return HttpResponse(nav_graph.SerializeToString(), content_type="application/octet-stream")
    else:
        return HttpResponse(json_format.MessageToJson(nav_graph), content_type="application/json")


def drawer(id):
    return Particle(
        id=id,
        modalDrawer=ModalDrawerComponent(
            content=Particle(id="12345", label=TextComponent(content="screen1"))
        )
    )


def screen1():
    return Particle(
        id="screen1_destination",
        screen=ScreenComponent(
            route="screen1",
            content=Particle(id="screen1_text-id", label=TextComponent(content="screen1")),
            bottomBar=Particle(
                id="bottom",
                bottomBar=BottomBarComponent(
                    elements=[bottom_bar_item("bottom_bar_item_1", True),
                              bottom_bar_item("bottom_bar_item_1", False)
                              ],
                    selectedElement="bottom_bar_item_1"
                )
            ),
            topBar=Particle(
                id="top", topBar=TopBarComponent(
                    title=Particle(id="top_text-id", label=TextComponent(content="tab1")),
                    navigationIcon=Particle(id="icon", icon=DEFAULT_ARROW_BACK)
                )
            ),
            modalDrawer=drawer("drawer"),
        )
    )


def screen2():
    return Particle(
        id="screen2_destination", screen=ScreenComponent(
            route="screen2",
            content=Particle(id="screen2_text-id", label=TextComponent(content="screen2"))
        )
    )


def bottom_bar_item(id, selected):
    return Particle(
        id=id,
        bottomBarItem=BottomBarItemComponent(
            selected=selected,
            text=Particle(id=id + "_text-id", label=TextComponent(content="tab2"))
        )
    )
