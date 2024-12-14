import pygame

from scripts.event_dispatchers import get_dt


def move_by_wasd(
    position: pygame.Vector2, velocity: pygame.Vector2
) -> tuple[pygame.Vector2, pygame.Vector2]:
    keys = pygame.key.get_pressed()

    delta = pygame.Vector2()
    if keys[pygame.K_w]:
        delta.y = -1
    if keys[pygame.K_s]:
        delta.y = 1
    if keys[pygame.K_a]:
        delta.x = -1
    if keys[pygame.K_d]:
        delta.x = 1

    if delta:
        delta.normalize_ip()

    position += pygame.Vector2(velocity.x * delta.x, velocity.y * delta.y) * get_dt()
    return position, velocity
