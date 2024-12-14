import pygame
from loguru import logger

from src.state_enums import GameState


def initialize_menu_state(screen: pygame.Surface):
    logger.info("Entered Menu State")
    return []


def process_menu_state():
    keys = pygame.key.get_just_pressed()
    if keys[pygame.K_RETURN]:
        return GameState.GAME
