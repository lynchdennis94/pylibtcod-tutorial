#!/usr/bin/env python3
import copy

import tcod

import entity_factory
from engine import Engine
from entity import Entity
from procgen import generate_dungeon
from input_handlers import EventHandler

SCREEN_WIDTH: int = 80
SCREEN_HEIGHT: int = 50
MAP_WIDTH: int = 80
MAP_HEIGHT: int = 45
ROOM_MAX_SIZE: int = 10
ROOM_MIN_SIZE: int = 6
MAX_ROOMS: int = 30
MAX_MONSTERS_PER_ROOM: int = 2
TILESET: tcod.tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)


def main():
    event_handler: EventHandler = EventHandler()
    player = copy.deepcopy(entity_factory.player)
    root_console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")
    game_map = generate_dungeon(max_rooms=MAX_ROOMS, room_min_size=ROOM_MIN_SIZE, room_max_size=ROOM_MAX_SIZE,
                                map_width=MAP_WIDTH, map_height=MAP_HEIGHT,
                                max_monsters_per_room=MAX_MONSTERS_PER_ROOM, player=player)
    engine: Engine = Engine(event_handler=event_handler, player=player, game_map=game_map)

    with tcod.context.new_terminal(SCREEN_WIDTH, SCREEN_HEIGHT, tileset=TILESET, title="Python libtcod Tutorial",
                                   vsync=True) as context:
        while True:
            engine.render(root_console, context)
            engine.handle_events(tcod.event.wait())


if __name__ == '__main__':
    main()
