from typing import Iterable, Any

from tcod import Console
from tcod.context import Context
from tcod.map import compute_fov

from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler


class Engine:
    """Class that holds the engine actions needed to make the game play"""

    def __init__(self, event_handler: EventHandler, player: Entity, game_map: GameMap):
        self.event_handler = event_handler
        self.player = player
        self.game_map = game_map
        self.update_fov()

    def handle_events(self, events: Iterable[Any]) -> None:
        """Handle events that have occurred during the game"""
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue
            else:
                action.perform(self, self.player)

        self.update_fov()

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view"""
        self.game_map.visible[:] = compute_fov(self.game_map.tiles["transparent"], (self.player.x, self.player.y),
                                               radius=8)
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console, context: Context) -> None:
        """Render entities on the console"""
        # Draw the map
        self.game_map.render(console)

        context.present(console)
        console.clear()
