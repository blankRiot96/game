from typing import Any, Callable

import pygame
from loguru import logger

from scripts.input_motions import move_by_wasd
from scripts.motion_patterns import circular_loop_position, horizontal_loop_position
from scripts.rendering import render_on_layer
from src.components import add_process, process
from src.entities import ComponentSchema, EntityType, add_entity
from src.state_enums import GameState


def initialize_game_state(screen: pygame.Surface) -> tuple[dict, dict]:
    logger.info("Entered Game State")

    components: dict[str, list[Any]] = {
        attr: [] for attr in ComponentSchema.__dataclass_fields__
    }
    entity_indeces: dict[EntityType, int] = {}
    processes: dict[int, list[Callable]] = {i: [] for i in range(len(EntityType))}

    image = pygame.Surface((50, 50))
    image.fill("red")
    add_entity(
        EntityType.PLAYER,
        ComponentSchema(
            position=pygame.Vector2(100, 100),
            image=image,
            hitbox=pygame.Rect((100, 100, 50, 50)),
            layer=screen,
            velocity=pygame.Vector2(500, 500),
        ),
        components,
        entity_indeces,
    )

    image = pygame.Surface((25, 25))
    image.fill("yellow")
    add_entity(
        EntityType.BEE,
        ComponentSchema(
            position=pygame.Vector2(),
            center=pygame.Vector2(600, 300),
            radians=0.0,
            angular_velocity=3.0,
            image=image,
            layer=screen,
            radius=100,
            direction=1,
            movement_points=[pygame.Vector2(50, 0), pygame.Vector2(700, 0)],
            velocity=pygame.Vector2(400, 0),
        ),
        components,
        entity_indeces,
    )

    image = pygame.Surface((50, 50))
    image.fill("blue")
    add_entity(
        EntityType.ENEMY,
        ComponentSchema(
            position=pygame.Vector2(200, 100),
            image=image,
            direction=1,
            layer=screen,
            movement_points=[pygame.Vector2(50, 0), pygame.Vector2(700, 0)],
            velocity=pygame.Vector2(400, 0),
        ),
        components,
        entity_indeces,
    )

    add_process(
        processes, [EntityType.BEE], entity_indeces, callback=circular_loop_position
    )
    add_process(
        processes,
        [EntityType.ENEMY, EntityType.BEE],
        entity_indeces,
        callback=horizontal_loop_position,
    )
    add_process(processes, [EntityType.PLAYER], entity_indeces, callback=move_by_wasd)

    add_process(
        processes,
        [EntityType.PLAYER, EntityType.ENEMY, EntityType.BEE],
        entity_indeces,
        callback=render_on_layer,
    )

    return components, processes


def process_game_state(components, processes):
    process(components, processes)

    keys = pygame.key.get_just_pressed()
    if keys[pygame.K_RETURN]:
        return GameState.MENU
