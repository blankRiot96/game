import pygame

clock = pygame.Clock()


class _Event:
    dt: float = 0.0
    events: list[pygame.Event] = []


def get_dt_ms() -> float:
    return _Event.dt


def get_dt(new_frame: bool = False) -> float:
    if new_frame:
        _Event.dt = clock.tick()

    return _Event.dt / 1000


def get_events(new_frame: bool = False):
    if new_frame:
        _Event.events = pygame.event.get()

    return _Event.events


def get_clock() -> pygame.Clock:
    return clock
