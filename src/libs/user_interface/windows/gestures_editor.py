from src.utils import *

class GesturesEditor:
    def __init__(self, on_button_pressed: callable, on_remove_gesture_pressed: callable, on_retrain_pressed: callable):
        self.callback = on_button_pressed  # Assign the button pressed callback function
        self.retrain = on_retrain_pressed  # Assign the retrain callback function
        self.remove = on_remove_gesture_pressed  # Assign the remove gesture callback function

    def create(self) -> None:
        self.window = Create.window(1000, 600)  # Create a window with specified dimensions
        self.canvas = Create.canvas(self.window, 600, 1000)  # Create a canvas within the window

        self.image_image_1 = Create.image(1, "image_1")  # Load the first image
        self.image_image_2 = Create.image(1, "image_2")  # Load the second image
        self.image_image_3 = Create.image(1, "image_4")  # Load the third image
        self.button_image_1 = Create.image(1, "button_1")  # Load the first button image
        self.button_image_2 = Create.image(1, "button_2")  # Load the second button image
        self.button_image_3 = Create.image(1, "button_3")  # Load the third button image
        self.button_image_4 = Create.image(1, "button_5")  # Load the fourth button image

        self.count = 0 # Initialize a counter for input fields
        self.gestures = os.listdir(DATASETS_PATH)  # List all files in the datasets path

        Create.frame(
            self.canvas,
            500.0,
            300.0,
            self.image_image_1  # Create a frame on the canvas with the first image
        )

        Create.button(
            self.button_image_1,
            35.0,
            35.0,
            70.0,
            70.0,
            lambda: self.callback(0)  # Create a button that triggers the callback with a specific argument
        )

        Create.button(
            self.button_image_2,
            895.0,
            35.0,
            70.0,
            70.0,
            lambda: self.callback(3, False, False)  # Create a button that triggers the callback with different arguments
        )

        Create.button(
            self.button_image_3,
            795.0,
            35.0,
            70.0,
            70.0,
            self.retrain  # Create a button that triggers the retrain function
        )

        for file in self.gestures:
            if file == 'None':  # Skip if the file is named 'None'
                continue

            self.count += 1
            x_distance = 500 if self.count > 3 else 0  # Determine x position based on count
            y_distance = (165 * (self.count - 4)) if self.count > 3 else (165 * (self.count - 1))  # Determine y position based on count

            Create.frame(
                self.canvas,
                250.0+x_distance,
                195.0+y_distance,
                self.image_image_2  # Create a frame for each gesture
            )

            Create.label(
                self.canvas,
                136.0+x_distance,
                173.0+y_distance,
                file,
                36  # Create a label for each gesture file
            )

            Create.button(
                self.button_image_4,
                285.0+x_distance,
                160.0+y_distance,
                180.0,
                70.0,
                lambda data=file: self.remove(data)  # Create a button to remove the gesture
            )

            Create.frame(
                self.canvas,
                70.0+x_distance,
                195.0+y_distance,
                self.image_image_3  # Create another frame for visual separation
            )

        Create.label(
            self.canvas,
            290.0,
            46.0,
            'Управление жестами',  # Create a title label for the gesture management
            40
        )

        self.window.mainloop()  # Start the main event loop for the window