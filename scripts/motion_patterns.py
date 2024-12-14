import math
from typing import Literal

import pygame

from scripts.event_dispatchers import get_dt


def circular_loop_position(
    position: pygame.Vector2,
    center: pygame.Vector2,
    radians: float,
    angular_velocity: float,
    radius: float,
):
    dt = get_dt()

    radians += angular_velocity * dt
    position.x = center.x + math.cos(radians) * radius
    position.y = center.y + math.sin(radians) * radius

    return position, center, radians, angular_velocity, radius


def horizontal_loop_position(
    position: pygame.Vector2,
    direction: Literal[-1, 1],
    movement_points: list[pygame.Vector2],
    velocity: pygame.Vector2,
) -> tuple[pygame.Vector2, Literal[-1, 1]]:
    dt = get_dt()
    position.x += velocity.x * direction * dt
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
