from particle.base_particle import BaseParticle
from particle.protos.particle import TextComponent, Particle, \
    BottomBarComponent, TopBarComponent, ScreenComponent, DEFAULT_ARROW_BACK, ModalDrawerComponent, \
    BottomBarItemComponent


class FirstScreen(BaseParticle):

    def __init__(self):
        data = _render()
        self.particle = data
        super().__init__(data)


def _render():
    return Particle(
        id="screen1_destination",
        screen=ScreenComponent(
            route="screen1",
            content=Particle(id="screen1_text-id", label=TextComponent(content="screen1")),
            bottomBar=Particle(
                id="bottom",
                bottomBar=BottomBarComponent(
                    elements=[__bottom_bar_item("bottom_bar_item_1", True),
                              __bottom_bar_item("bottom_bar_item_1", False)
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
            modalDrawer=__drawer("drawer"),
        )
    )


def __bottom_bar_item(id, selected):
    return Particle(
        id=id,
        bottomBarItem=BottomBarItemComponent(
            selected=selected,
            text=Particle(id=id + "_text-id", label=TextComponent(content="tab2"))
        )
    )


def __drawer(id):
    return Particle(
        id=id,
        modalDrawer=ModalDrawerComponent(
            content=Particle(id="12345", label=TextComponent(content="screen1"))
        )
    )
