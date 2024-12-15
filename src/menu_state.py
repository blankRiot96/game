from dataclasses import dataclass

import mili
import pygame
from loguru import logger

from scripts.event_dispatchers import get_clock
from src.state_enums import GameState

clock = get_clock()


BTN_WIDTH = 200
BTN_HEIGHT = 100
N_ROWS = 2
N_COLS = 3
N_BTNS = N_ROWS * N_COLS


@dataclass
class MiliData:
    button_animations: list[mili.animation.StatusAnimation]


def initialize_menu_state(screen: pygame.Surface):
    logger.info("Entered Menu State")

    gui = mili.MILI(screen)

    base_btn_value = BTN_WIDTH
    mili_data = MiliData(
        button_animations=[
            mili.animation.StatusAnimation(
                base_value=base_btn_value,
                hover_value=base_btn_value * 1.2,
                press_value=base_btn_value * 1.1,
                duration_ms=500,
                value_type="number",
                easing=mili.animation.EaseOvershoot(),
                update_id=f"btn-{i}",
            )
            for i in range(1, N_BTNS + 1)
        ]
    )

    logger.debug(f"{len(mili_data.button_animations)=}")

    return gui, mili_data


def process_menu_state(gui: mili.MILI, mili_data: MiliData):
    keys = pygame.key.get_just_pressed()
    if keys[pygame.K_RETURN]:
        return GameState.GAME

    mili.animation.update_all()
    gui.start(mili.CENTER)

    with gui.begin(
        (0, 0, (BTN_WIDTH + 10) * N_COLS, (BTN_HEIGHT + 10) * N_ROWS),
        {
            "grid": True,
            "clip_draw": False,
            # "grid_align": "max_spacing",
            # "anchor": "max_spacing",
        },
    ) as main:
        gui.rect({"color": (50, 50, 50)})
        for i in range(1, N_BTNS + 1):
            with gui.begin(
                (0, 0, BTN_WIDTH, BTN_HEIGHT),
                {"anchor": "center", "clip_draw": False},
            ) as sub:
                style = {"update_id": f"btn-{i}", "align": "center"}
                interaction = gui.element(
                    (
                        0,
                        0,
                        mili_data.button_animations[i - 1].value,
                        mili_data.button_animations[i - 1].value / 2,
                    ),
                    style,
                )
                gui.rect({"color": "seagreen"})

                if interaction.hovered:
                    style["z"] = 2
                    gui.rect({"color": (50, 100, 50)})

                if interaction.left_pressed:
                    gui.rect({"color": (100, 150, 100)})

                gui.text(str(i))
                if interaction.left_just_pressed:
                    logger.trace(f"Clicked {i}")

    gui.update_draw()
