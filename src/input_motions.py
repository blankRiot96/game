import pygame


def move_by_wasd(
    position: pygame.Vector2, velocity: pygame.Vector2
) -> tuple[pygame.Vector2, pygame.Vector2]:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        position.y -= velocity.y
    if keys[pygame.K_s]:
        position.y += velocity.y
    if keys[pygame.K_a]:
        position.x -= velocity.x
    if keys[pygame.K_d]:
        position.x += velocity.x

    return position, velocity
