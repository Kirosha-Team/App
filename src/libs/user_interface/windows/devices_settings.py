from src.libs.user_interface.assets import *
from src.libs.communicator import *
from src.utils import *

class DevicesSettings:
    def __init__(self, on_button_pressed: callable, on_save_pressed: callable):
        self.callback = on_button_pressed
        self.save = on_save_pressed

        self.registry = Registry()

    def create(self, data: list) -> None:
        self.roots = create_default_window()
        self.assets = load_default_components()

        self.count = 0
        self.input_data = {}

        Create.frame(
            self.roots["canvas"],
            500.0,
            300.0,
            self.assets["background_image"]
        )

        Create.button(
            self.assets["exit_button_image"],
            35.0,
            35.0,
            70.0,
            70.0,
            lambda: self.callback(2, False, False)  # Return to the devices editor window
        )

        Create.button(
            self.assets["retrain_button_image"],
            895.0,
            35.0,
            70.0,
            70.0,
            lambda: self.save(data, self.input_data)
        )

        for line in data[3:]:
            key, value = line.split('=')

            self.count += 1

            x_distance = 500 if self.count > 3 else 0
            y_distance = (165 * (self.count - 4)) if self.count > 3 else (165 * (self.count - 1))

            Create.frame(
                self.roots["canvas"],
                250.0 + x_distance,
                195.0 + y_distance,
                self.assets["button_background_image"]
            )

            Create.label(
                self.roots["canvas"],
                136.0 + x_distance,
                173.0 + y_distance,
                key,
                36
            )

            Create.frame(
                self.roots["canvas"],
                375.0 + x_distance,
                195.0 + y_distance,
                self.assets["button_image"]
            )

            input = Create.input_box(
                290 + x_distance,
                165 + y_distance,
                170,
                60
            )

            input.insert(0, value)

            self.input_data[key] = input

            Create.frame(
                self.roots["canvas"],
                70.0 + x_distance,
                195.0 + y_distance,
                self.assets["sparkle_image"]
            )

        Create.label(
            self.roots["canvas"],
            340.0,
            46.0,
            f'{data[2]}',
            40
        )