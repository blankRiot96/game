import pygame
from loguru import logger

from src.state_dispatcher import dispatch_state, process_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 800), vsync=1)
    clock = pygame.Clock()

    initial_state, state_processor = dispatch_state(screen)

    while True:
        dt = clock.tick()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                raise SystemExit

        screen.fill("black")

        process_state(initial_state, state_processor)
        pygame.display.flip()


if __name__ == "__main__":
    main()
