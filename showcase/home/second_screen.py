from particle.protos.particle import TextComponent, Particle, \
    ScreenComponent, TopBarComponent, DEFAULT_ARROW_BACK


def SecondScreen():
    return Particle(
        id="screen2_destination", screen=ScreenComponent(
            route="screen2",
            topBar=Particle(
                id="top", topBar=TopBarComponent(
                    title=Particle(id="top_text-id", label=TextComponent(content="tab1")),
                    navigationIcon=Particle(id="icon", icon=DEFAULT_ARROW_BACK)
                )
            ),
            content=Particle(id="screen2_text-id", label=TextComponent(content="screen2"))
        )
    )
