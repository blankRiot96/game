from typing import Literal

import pygame


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
