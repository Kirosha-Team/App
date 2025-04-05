from src.libs.user_interface.assets import *
from src.utils import *


class GesturesEditor:
    def __init__(
        self,
        on_button_pressed: callable,
        on_remove_gesture_pressed: callable,
        on_retrain_pressed: callable,
    ):
        self.callback = on_button_pressed
        self.retrain = on_retrain_pressed
        self.remove = on_remove_gesture_pressed

    def create(
        self,
    ) -> None:
        self.roots = (
            create_default_window()
        )
        self.assets = (
            load_default_components()
        )

        self.count = 0
        self.gestures = os.listdir(
            DATASETS_PATH
        )

        Create.frame(
            self.roots[
                "canvas"
            ],
            500.0,
            300.0,
            self.assets[
                "background_image"
            ],
        )

        Create.button(
            self.assets[
                "exit_button_image"
            ],
            35.0,
            35.0,
            70.0,
            70.0,
            lambda: self.callback(
                0
            ),  # Return to the main menu window
        )

        Create.button(
            self.assets[
                "add_button_image"
            ],
            895.0,
            35.0,
            70.0,
            70.0,
            lambda: self.callback(
                3,
                False,
                False,
            ),  # Open the gesture name window
        )

        Create.button(
            self.assets[
                "retrain_button_image"
            ],
            795.0,
            35.0,
            70.0,
            70.0,
            self.retrain,
        )

        for file in (
            self.gestures
        ):
            if (
                file
                == "None"
            ):
                continue

            self.count += 1
            x_distance = (
                500
                if self.count
                > 3
                else 0
            )
            y_distance = (
                (
                    165
                    * (
                        self.count
                        - 4
                    )
                )
                if self.count
                > 3
                else (
                    165
                    * (
                        self.count
                        - 1
                    )
                )
            )

            Create.frame(
                self.roots[
                    "canvas"
                ],
                250.0
                + x_distance,
                195.0
                + y_distance,
                self.assets[
                    "button_background_image"
                ],
            )

            Create.label(
                self.roots[
                    "canvas"
                ],
                136.0
                + x_distance,
                173.0
                + y_distance,
                file,
                36,
            )

            Create.button(
                self.assets[
                    "remove_button_image"
                ],
                285.0
                + x_distance,
                160.0
                + y_distance,
                180.0,
                70.0,
                lambda data=file: self.remove(
                    data
                ),
            )

            Create.frame(
                self.roots[
                    "canvas"
                ],
                70.0
                + x_distance,
                195.0
                + y_distance,
                self.assets[
                    "hand_image"
                ],
            )

        Create.label(
            self.roots[
                "canvas"
            ],
            290.0,
            46.0,
            "Управление жестами",
            40,
        )
