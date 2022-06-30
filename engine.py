from typing import Set, Iterable, Any

from tcod import Console
from tcod.context import Context

from actions import MovementAction, EscapeAction
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler


class Engine:
    """Class that holds the engine actions needed to make the game play"""

    def __init__(self, entities: Set[Entity], event_handler: EventHandler, player: Entity, game_map: GameMap):
        self.entities = entities
        self.event_handler = event_handler
        self.player = player
        self.game_map = game_map

    def handle_events(self, events: Iterable[Any]) -> None:
        """Handle events that have occurred during the game"""
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue
            else:
                action.perform(self, self.player)

    def render(self, console: Console, context: Context) -> None:
        """Render entities on the console"""
        # Draw the map
        self.game_map.render(console)

        # Add the individual entities
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)
        console.clear()
