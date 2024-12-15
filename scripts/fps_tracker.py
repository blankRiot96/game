import pygame
from pygame.typing import Point

from scripts.event_dispatchers import get_clock
from scripts.timers import Time

pygame.font.init()
fps_font = pygame.Font(size=32)
clock = get_clock()


def get_fps_surf(fps: float | None = None):
    if fps is None:
        fps = clock.get_fps()
    return fps_font.render(f"{fps:.0f}", True, "green")


class _FrameInfo:
    fps_in_prev_frames: list[float] = []
    fps_surf: pygame.Surface = get_fps_surf()
    fps_refresh_timer = Time(1.0)


def display_current_fps(screen: pygame.Surface, dest: Point = (0, 0)):
    screen.blit(get_fps_surf(), dest)


def display_mean_fps(
    screen: pygame.Surface, seconds: float, dest: Point = (0, 0)
) -> None:
    _FrameInfo.fps_refresh_timer.time_to_pass = seconds
    _FrameInfo.fps_in_prev_frames.append(clock.get_fps())
    if _FrameInfo.fps_refresh_timer.tick():
        mean_fps = sum(_FrameInfo.fps_in_prev_frames) / len(
            _FrameInfo.fps_in_prev_frames
        )
        _FrameInfo.fps_surf = get_fps_surf(mean_fps)
        _FrameInfo.fps_in_prev_frames.clear()

    screen.blit(_FrameInfo.fps_surf, dest)
