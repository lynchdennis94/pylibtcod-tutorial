#!/usr/bin/env python3
import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

SCREEN_WIDTH: int = 80
SCREEN_HEIGHT: int = 50
MAP_WIDTH: int = 80
MAP_HEIGHT: int = 45
TILESET: tcod.tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)


def main():
    player_x: int = int(SCREEN_WIDTH / 2)
    player_y: int = int(SCREEN_HEIGHT / 2)
    event_handler: EventHandler = EventHandler()
    player = Entity(player_x, player_y, "@", (255, 255, 255))
    root_console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")
    npc = Entity(player_x - 2, player_y - 2, "X", (0, 255, 0))
    entities = {player, npc}
    game_map = GameMap(MAP_WIDTH, MAP_HEIGHT)
    engine: Engine = Engine(entities=entities, event_handler=event_handler, player=player, game_map=game_map)

    with tcod.context.new_terminal(SCREEN_WIDTH, SCREEN_HEIGHT, tileset=TILESET, title="Python libtcod Tutorial",
                                   vsync=True) as context:
        while True:
            engine.render(root_console, context)
            engine.handle_events(tcod.event.wait())


if __name__ == '__main__':
    main()
