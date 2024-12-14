from collections.abc import Callable
from functools import partial

import pygame

from src.game_state import initialize_game_state, process_game_state
from src.menu_state import initialize_menu_state, process_menu_state
from src.state_enums import GameState


def dispatch_state(state: GameState, screen: pygame.Surface) -> Callable:
    if state == GameState.GAME:
        return partial(process_game_state, *initialize_game_state(screen))
    elif state == GameState.MENU:
        return partial(process_menu_state, *initialize_menu_state(screen))


def process_state(
    new_state: GameState | None,
    screen: pygame.Surface,
    state_processor: Callable | None = None,
) -> tuple[GameState | None, Callable]:

    if new_state is not None:
        state_processor = dispatch_state(new_state, screen)

    return state_processor(), state_processor
