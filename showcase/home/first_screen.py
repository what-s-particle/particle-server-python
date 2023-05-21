from particle.protos.particle import TextComponent, Particle, \
    BottomBarComponent, TopBarComponent, ScreenComponent, ModalDrawerComponent, \
    BottomBarItemComponent, Interaction, TAP_EVENT, NavItemSelectedAction, Action


def FirstScreen():
    return Particle(
        id="screen1_destination",
        screen=ScreenComponent(
            route="screen1",
            content=Particle(id="screen1_text-id", label=TextComponent(content="screen1")),
            bottomBar=Particle(
                id="bottom",
                bottomBar=BottomBarComponent(
                    elements=[__bottom_bar_item_component("bottom-bar-item-1"),
                              __bottom_bar_item_custom("bottom-bar-item-2")
                              ],
                    selectedElement="bottom-bar-item-1"
                )
            ),
            topBar=Particle(
                id="top", topBar=TopBarComponent(
                    title=Particle(id="top_text-id", label=TextComponent(content="Top bar"))
                )
            ),
            modalDrawer=__drawer("drawer"),
        )
    )


def __bottom_bar_item_component(id):
    return Particle(
        id=id,
        bottomBarItem=BottomBarItemComponent(
            selected=True,
            text=Particle(id=id + "-text", label=TextComponent(content="Component"))
        ),
        interactions=[Interaction(event=[TAP_EVENT],
                                  action=[Action(navItemSelected=NavItemSelectedAction(target="bottom", selectId=id))])]
    )


def __bottom_bar_item_custom(id):
    return Particle(
        id=id,
        bottomBarItem=BottomBarItemComponent(
            selected=False,
            text=Particle(id=id + "-text", label=TextComponent(content="Custom"))
        ),
        interactions=[Interaction(event=[TAP_EVENT],
                                  action=[Action(navItemSelected=NavItemSelectedAction(target="bottom", selectId=id))])]
    )


def __drawer(id):
    return Particle(
        id=id,
        modalDrawer=ModalDrawerComponent(
            content=Particle(id="12345", label=TextComponent(content="screen1"))
        )
    )
