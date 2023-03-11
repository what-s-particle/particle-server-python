from django.http import HttpResponse
from google.protobuf import json_format

from particle.protos.particle import Modifier, TextComponent, ElementComponent, Particle, LayoutComponent, \
    BottomBarComponent, BottomBarItemComponent, TopBarComponent, ScreenComponent, NavGraphComponent, \
    ModalDrawerComponent


def index(request):
    modifier = Modifier(visible=True, clickable=True)
    interactions = []

    screens = [screen1(), screen2()]

    nav_graph = Particle(
        id="nav_graph",
        layout=LayoutComponent(
            navGraph=NavGraphComponent(startDestination="screen1", screens=screens)
        ),
        interactions=interactions,
        modifier=modifier)

    if request.content_type == "application/octet-stream":
        return HttpResponse(nav_graph.SerializeToString(), content_type="application/octet-stream")
    else:
        return HttpResponse(json_format.MessageToJson(nav_graph), content_type="application/json")


def drawer(id):
    return Particle(
        id=id, layout=LayoutComponent(
            modalDrawer=ModalDrawerComponent(
                content=Particle(id="12345", element=ElementComponent(label=TextComponent(content="screen1")))
            )
        )
    )


def screen1():
    component = TextComponent(content="screen1")
    element = ElementComponent(label=component)

    return Particle(
        id="screen1_destination", layout=LayoutComponent(
            screen=ScreenComponent(
                route="screen1",
                content=Particle(id="screen1_text-id", element=element),
                bottomBar=bottom_bar("bottom"),
                topBar=top_bar_item("top"),
                modalDrawer=drawer("drawer"),
            )
        )
    )


def screen2():
    component = TextComponent(content="screen2")
    element = ElementComponent(label=component)
    return Particle(
        id="screen2_destination", layout=LayoutComponent(
            screen=ScreenComponent(
                route="screen2",
                content=Particle(id="screen2_text-id", element=element)
            )
        )
    )


def bottom_bar(id):
    return Particle(
        id=id, layout=LayoutComponent(
            bottomBar=BottomBarComponent(
                elements=[bottom_bar_item("bottom_bar_item_1", True),
                          bottom_bar_item("bottom_bar_item_1", False)
                          ],
                selectedElement="bottom_bar_item_1"
            )
        )
    )


def bottom_bar_item(id, selected):
    component = TextComponent(content="tab2")
    element = ElementComponent(label=component)

    return Particle(
        id=id, element=ElementComponent(
            bottomBarItem=BottomBarItemComponent(
                selected=selected,
                text=Particle(id=id + "_text-id", element=element)
            )
        )
    )


def top_bar_item(id):
    component = TextComponent(content="tab2")
    element = ElementComponent(label=component)

    return Particle(
        id=id, layout=LayoutComponent(
            topBar=TopBarComponent(
                title=Particle(id=id + "_text-id", element=element)
            )
        )
    )
