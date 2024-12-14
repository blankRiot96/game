import enum
from dataclasses import dataclass
from typing import Literal

import pygame
from loguru import logger


class EntityType(enum.Enum):
    PLAYER = enum.auto()
    ENEMY = enum.auto()
    BEE = enum.auto()


@dataclass
class ComponentSchema:
    position: pygame.Vector2 | None = None
    image: pygame.Surface | None = None
    hitbox: pygame.Rect | None = None
    direction: Literal[1, -1] | None = None
    layer: pygame.Surface | None = None
    movement_points: list[pygame.Vector2] | None = None
    velocity: pygame.Vector2 | None = None
    angular_velocity: float | None = None
    radians: float | None = None
    radius: float | None = None
    center: pygame.Vector2 | None = None


def add_entity(
    entity_type: EntityType,
    component_schema: ComponentSchema,
    components,
    entity_indeces,
) -> None:

    entity_indeces[entity_type] = len(entity_indeces)

    for attr in ComponentSchema.__dataclass_fields__:
        components[attr].append(getattr(component_schema, attr))

    logger.debug(f"Added Entity `{entity_type.name}`")


if __name__ == "__main__":
    print(list(ComponentSchema.__dataclass_fields__))
