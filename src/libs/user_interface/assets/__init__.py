"""
NAME: assets.py
DESC: ui components loader for different windows
"""

from src.utils import (
    Create,
)


def create_default_window():
    window = Create.window(
        1000,
        600,
    )
    canvas = Create.canvas(
        window,
        600,
        1000,
    )

    return {
        "window": window,
        "canvas": canvas,
    }


def create_box_window():
    window = Create.window(
        400,
        250,
    )
    canvas = Create.canvas(
        window,
        250,
        400,
    )

    return {
        "window": window,
        "canvas": canvas,
    }


def load_main_menu_components():
    return {
        "background_image": Create.image(
            0,
            "image_1",
        ),
        "split_box_image": Create.image(
            0,
            "image_2",
        ),
        "gestures_button_image": Create.image(
            0,
            "button_1",
        ),
        "devices_button_image": Create.image(
            0,
            "button_2",
        ),
        "info_button_image": Create.image(
            0,
            "button_3",
        ),
    }


def load_default_components():
    return {
        "background_image": Create.image(
            1,
            "image_1",
        ),
        "button_background_image": Create.image(
            1,
            "image_2",
        ),
        "device_image": Create.image(
            1,
            "image_3",
        ),
        "hand_image": Create.image(
            1,
            "image_4",
        ),
        "sparkle_image": Create.image(
            1,
            "image_5",
        ),
        "exit_button_image": Create.image(
            1,
            "button_1",
        ),
        "add_button_image": Create.image(
            1,
            "button_2",
        ),
        "retrain_button_image": Create.image(
            1,
            "button_3",
        ),
        "change_button_image": Create.image(
            1,
            "button_4",
        ),
        "remove_button_image": Create.image(
            1,
            "button_5",
        ),
        "button_image": Create.image(
            1,
            "button_6",
        ),
    }


def load_box_components():
    return {
        "background_image": Create.image(
            2,
            "image_1",
        ),
        "save_button_image": Create.image(
            2,
            "button_1",
        ),
        "cancel_button_image": Create.image(
            2,
            "button_2",
        ),
    }
