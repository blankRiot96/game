import pygame
from loguru import logger

from scripts.event_dispatchers import get_clock, get_dt, get_events
from scripts.state_dispatcher import dispatch_state, process_state
from src.state_enums import GameState


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 800))
    clock = get_clock()
    fps_font = pygame.Font(size=32)

    new_state = GameState.GAME
    state_processor = None

    while True:
        events = get_events(new_frame=True)
        dt = get_dt(new_frame=True)
        for event in events:
            if event.type == pygame.QUIT:
                raise SystemExit

        screen.fill("black")

        new_state, state_processor = process_state(new_state, screen, state_processor)
        screen.blit(fps_font.render(f"{clock.get_fps():.0f}", True, "green"), (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
