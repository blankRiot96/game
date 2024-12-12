from collections.abc import Callable
from typing import Any, Literal

import pygame
from loguru import logger

from src.entities import ComponentSchema, EntityType


def add_entity(
    entity_type: EntityType,
    component_schema: ComponentSchema,
    components,
    entity_indeces,
) -> None:

    entity_indeces[entity_type] = len(entity_indeces)

    for attr in ComponentSchema.__dataclass_fields__:
        components[attr].append(getattr(component_schema, attr))


def horizontal_loop_position(
    position: pygame.Vector2,
    direction: Literal[-1, 1],
    movement_points: list[pygame.Vector2],
    velocity: float,
) -> tuple[pygame.Vector2, Literal[-1, 1]]:
    position.x += velocity.x * direction
    if position.x >= movement_points[1].x or position.x <= movement_points[0].x:
        direction *= -1

    return (
        pygame.Vector2(
            pygame.math.clamp(position.x, movement_points[0].x, movement_points[1].x),
            position.y,
        ),
        direction,
        movement_points,
        velocity,
    )


def process(
    components: dict[str, list[Any]],
    processes: dict[int, list[Callable]],
):

    for component_index, process_list in processes.items():
        for process in process_list:
            components_required = process.__code__.co_varnames
            process_arguments = {
                component_name: components[component_name][component_index]
                for component_name in components_required
            }
            modified_components = process(**process_arguments)

            if modified_components is None:
                continue

            for component_name, modified_component in zip(
                components_required, modified_components
            ):
                components[component_name][component_index] = modified_component


def add_process(
    processes: dict[int, list[Callable]],
    entities: list[EntityType],
    entity_indeces: dict[EntityType, int],
    callback: Callable,
) -> None:
    for entity_type in entities:
        processes[entity_indeces.get(entity_type)].append(callback)


def render_on_layer(
    layer: pygame.Surface, image: pygame.Surface, position: pygame.Vector2
):
    layer.blit(image, position)


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 800))

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
            velocity=pygame.Vector2(1, 0),
        ),
        components,
        entity_indeces,
    )

    add_process(
        processes, [EntityType.ENEMY], entity_indeces, callback=horizontal_loop_position
    )
    add_process(
        processes,
        [EntityType.PLAYER, EntityType.ENEMY],
        entity_indeces,
        callback=render_on_layer,
    )

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                raise SystemExit

        screen.fill("black")

        process(components, processes)
        pygame.display.flip()


if __name__ == "__main__":
    main()
