import time, datetime

from src.libs.user_interface.assets import *
from src.utils import *

class MainMenu:
    def __init__(self, on_button_pressed: callable, on_display_info_pressed: callable):
        self.callback = on_button_pressed
        self.display = on_display_info_pressed

        self.time = None
        self.date = None
        self.weather = None

    def create(self) -> None:
        self.roots = create_default_window()
        self.assets = load_main_menu_components()

        def update() -> None:
            current_time = time.strftime('%H:%M')

            date = datetime.date.today()
            weekday = WEEKDAYS[datetime.date.weekday(date)]

            self.roots["canvas"].itemconfig(tagOrId=self.time, text=current_time)
            self.roots["canvas"].itemconfig(tagOrId=self.date, text=f'{weekday}.\n{date.day}')

            self.roots["window"].after(UPDATE_DELAY, update)

        Create.frame(
            self.roots["canvas"],
            500.0,
            300.0,
            self.assets["background_image"]
        )

        Create.frame(
            self.roots["canvas"],
            335.0,
            520.0,
            self.assets["split_box_image"]
        )

        Create.button(
            self.assets["gestures_button_image"],
            475.0,
            475.0,
            90.0,
            90.0,
            lambda: self.callback(1, False, False)  # Open the gestures editor window
        )

        Create.button(
            self.assets["devices_button_image"],
            585.0,
            475.0,
            90.0,
            90.0,
            lambda: self.callback(2, False, False)  # Open the devices editor window
        )

        Create.button(
            self.assets["info_button_image"],
            695.0,
            475.0,
            90.0,
            90.0,
            lambda: self.display() # Open the info window
        )

        self.time = Create.label(
            self.roots["canvas"],
            313.0,
            63.0,
            '',
            128
        )

        self.date = Create.label(
            self.roots["canvas"],
            253.0,
            486.0,
            '',
            28
        )

        self.weather = Create.label(
            self.roots["canvas"],
            364.0,
            503.0,
            '~~°C',
            28
        )

        update()