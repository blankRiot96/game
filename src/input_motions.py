import pygame

from src.event_dispatchers import get_dt


def move_by_wasd(
    position: pygame.Vector2, velocity: pygame.Vector2
) -> tuple[pygame.Vector2, pygame.Vector2]:
    keys = pygame.key.get_pressed()

    delta = pygame.Vector2()
    if keys[pygame.K_w]:
        delta.y -= velocity.y
    if keys[pygame.K_s]:
        delta.y += velocity.y
    if keys[pygame.K_a]:
        delta.x -= velocity.x
    if keys[pygame.K_d]:
        delta.x += velocity.x

    position += delta * get_dt()
    return position, velocity
