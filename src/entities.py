import enum
from dataclasses import dataclass
from typing import Literal

import pygame

from src.hardware_input import HardwareInput


class EntityType(enum.Enum):
    PLAYER = enum.auto()
    ENEMY = enum.auto()


@dataclass
class ComponentSchema:
    position: pygame.Vector2 | None = None
    image: pygame.Surface | None = None
    hitbox: pygame.Rect | None = None
    direction: Literal[1, -1] | None = None
    layer: pygame.Surface | None = None
    movement_points: list[pygame.Vector2] | None = None
    velocity: pygame.Vector2 | None = None


if __name__ == "__main__":
    print(list(ComponentSchema.__dataclass_fields__))
