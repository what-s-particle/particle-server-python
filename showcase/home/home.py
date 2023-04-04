from particle.base_particle import BaseParticle
from particle.protos.particle import Modifier, Particle, NavGraphComponent, ScreenComponent, TextComponent
from showcase.home.first_screen import FirstScreen


class HomeScreen(BaseParticle):

    def __init__(self):
        data = _render()
        self.particle = data,
        super().__init__(data)


def _render():
    modifier = Modifier(visible=True, clickable=True)
    interactions = []
    screen1 = FirstScreen().particle
    screens = [screen1, screen2()]
    data = Particle(
        id="nav_graph",
        interactions=interactions,
        modifier=modifier,
        navGraph=NavGraphComponent(startDestination="screen1", screens=screens)
    )
    return data


def screen2():
    return Particle(
        id="screen2_destination", screen=ScreenComponent(
            route="screen2",
            content=Particle(id="screen2_text-id", label=TextComponent(content="screen2"))
        )
    )
