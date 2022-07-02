from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class Action:
    """Generic Action class"""

    def perform(self, engine: Engine, entity: Entity) -> None:
        """
        Perform this action with the objects needed to determine its scope

        `engine` is the scope this action is performed in

        `entity` is the object performing the action

        This method must be overridden by Action subclasses
        """
        raise NotImplementedError()


class EscapeAction(Action):
    """Action implementation that represents escaping out of the program"""

    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()


class ActionWithDirection(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: Entity) -> None:
        raise NotImplementedError()


class MovementAction(ActionWithDirection):
    """Action implementation that represents player movement"""

    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return  # Destination is out of bounds, do nothing
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return  # Can't walk to that destination
        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return # Can't walk into a blocking entity

        entity.move(self.dx, self.dy)
