import mili
import pygame
from loguru import logger

from src.state_enums import GameState


def initialize_menu_state(screen: pygame.Surface):
    logger.info("Entered Menu State")

    gui = mili.MILI(screen)

    return [gui]


def process_menu_state(gui: mili.MILI):
    keys = pygame.key.get_just_pressed()
    if keys[pygame.K_RETURN]:
        return GameState.GAME

    gui.start(mili.CENTER)

    with gui.begin((0, 0, 800, 300)) as main:
        gui.rect({"color": (50, 50, 50)})
        for i in range(1, 11):
            interaction = gui.element((0, 0, 50, 50), {"grid_align": "max_spacing"})
            gui.rect({"color": "seagreen"})

            if interaction.hovered:
                gui.rect({"color": (50, 100, 50)})

            if interaction.left_pressed:
                gui.rect({"color": (100, 150, 100)})

            gui.text(str(i))
            if interaction.left_just_pressed:
                logger.trace(f"Clicked {i}")

    gui.update_draw()
