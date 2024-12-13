from collections.abc import Callable
from functools import partial

import pygame

from src.game_state import initialize_game_state, process_game_state
from src.state_enums import GameState


def dispatch_state(screen: pygame.Surface) -> tuple[GameState, Callable]:
    current_state = GameState.GAME

    if current_state == GameState.GAME:
        return current_state, partial(
            process_game_state, *initialize_game_state(screen)
        )


def process_state(initial_state: GameState, state_processor: Callable) -> None:
    if initial_state == GameState.GAME:
        state_processor()
