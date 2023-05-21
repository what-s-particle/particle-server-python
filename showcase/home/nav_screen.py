from particle.protos.particle import Modifier, Particle, NavGraphComponent
from typing import List


def NavScreen(screens: List[Particle]):
    modifier = Modifier(visible=True, clickable=True)
    interactions = []
    return Particle(
        id="nav_graph",
        interactions=interactions,
        modifier=modifier,
        navGraph=NavGraphComponent(startDestination="screen1", screens=screens)
    )
