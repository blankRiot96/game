import pygame


def render_on_layer(
    layer: pygame.Surface, image: pygame.Surface, position: pygame.Vector2
):
    layer.blit(image, position)
