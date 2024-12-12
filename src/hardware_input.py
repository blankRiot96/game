import pygame
from pygame.key import ScancodeWrapper


class HardwareInput:
    keys: ScancodeWrapper
    key_just_pressed: ScancodeWrapper
    key_just_released: ScancodeWrapper
    mouse_press: tuple[int, int, int]

    @staticmethod
    def update_all() -> None:
        HardwareInput.keys = pygame.key.get_pressed()
