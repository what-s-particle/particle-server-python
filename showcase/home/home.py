from particle.protos.particle import Modifier, Particle, NavGraphComponent, ScreenComponent, TextComponent
from showcase.home.screen1 import Screen1


class HomeScreen:

    @staticmethod
    def render():
        modifier = Modifier(visible=True, clickable=True)
        interactions = []

        screens = [Screen1.render(), screen2()]
        return Particle(
            id="nav_graph",
            interactions=interactions,
            modifier=modifier,
            navGraph=NavGraphComponent(startDestination="screen1", screens=screens)
        )


def screen2():
    return Particle(
        id="screen2_destination", screen=ScreenComponent(
            route="screen2",
            content=Particle(id="screen2_text-id", label=TextComponent(content="screen2"))
        )
    )
