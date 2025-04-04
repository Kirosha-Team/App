from src.libs.user_interface.assets import *
from src.utils import *

class GestureName:
    def __init__(self, on_button_pressed: callable, on_save_pressed: callable):
        self.save = on_save_pressed
        self.callback = on_button_pressed

    def create(self) -> None:
        self.roots = create_box_window()
        self.assets = load_box_components()

        Create.frame(
            self.roots["canvas"],
            200.0,
            125.0,
            self.assets["background_image"]
        )

        Create.button(
            self.assets["save_button_image"],
            10.0,
            170.0,
            180.0,
            70.0,
            lambda: self.save(self.entry.get()) # Close the gesture name window
        )

        Create.button(
            self.assets["cancel_button_image"],
            210.0,
            170.0,
            180.0,
            70.0,
            lambda: self.callback(1, False, False) # Return to the gestures editor window
        )

        self.entry = Create.input_box(
            15.0,
            70.0,
            370.0,
            68.0
        )