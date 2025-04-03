from src.libs.user_interface.assets import *
from src.libs.communicator import *
from src.utils import *

class DevicesEditor:
    def __init__(self, on_button_pressed: callable):
        self.callback = on_button_pressed
        self.registry = Registry()

    def create(self) -> None:
        self.roots = create_default_window()
        self.assets = load_default_components()

        self.count = 0
        self.devices = Registry.get_devices() or []

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
            lambda: self.callback(0)  # Return to the main menu window
        )

        Create.label(
            self.roots["canvas"],
            300.0,
            46.0,
            'Управление устройствами',
            40
        )

        for data in self.devices:
            name = data[2]

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
                name,
                36
            )

            Create.button(
                self.assets["change_button_image"],
                285.0 + x_distance,
                160.0 + y_distance,
                180.0,
                70.0,
                lambda device=data: self.callback(4, False, False, device) # Open the devices settings window
            )

            Create.frame(
                self.roots["canvas"],
                70.0 + x_distance,
                195.0 + y_distance,
                self.assets["device_image"]
            )