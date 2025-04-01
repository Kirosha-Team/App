from src.libs.communicator import *
from src.utils import *

class DevicesSettings:
    def __init__(self, on_button_pressed: callable, on_save_pressed: callable):
        self.callback = on_button_pressed  # Assign the callback function for button press
        self.save = on_save_pressed  # Assign the save function for saving data

        self.registry = Registry()  # Initialize the Registry instance

    def create(self, data: list) -> None:
        self.window = Create.window(1000, 600)  # Create a window with specified dimensions
        self.canvas = Create.canvas(self.window, 600, 1000)  # Create a canvas within the window

        self.image_image_1 = Create.image(1, "image_1")  # Load the first image
        self.image_image_2 = Create.image(1, "image_2")  # Load the second image
        self.image_image_3 = Create.image(1, "image_5")  # Load the third image
        self.button_image_1 = Create.image(1, "button_1")  # Load the first button image
        self.button_image_2 = Create.image(1, "button_6")  # Load the second button image
        self.button_image_3 = Create.image(1, "button_3")  # Load the third button image

        self.count = 0  # Initialize a counter for input fields
        self.input_data = {}  # Dictionary to store input data

        Create.frame(
            self.canvas,
            500.0,
            300.0,
            self.image_image_1  # Create a frame with the first image
        )

        Create.button(
            self.button_image_1,
            35.0,
            35.0,
            70.0,
            70.0,
            lambda: self.callback(2, False, False)  # Create a button that triggers the callback
        )

        Create.button(
            self.button_image_3,
            895.0,
            35.0,
            70.0,
            70.0,
            lambda: self.save(data, self.input_data)  # Create a button that saves data
        )

        for line in data[3:]:  # Iterate over the data starting from the fourth line
            key, value = line.split('=')  # Split each line into key and value

            self.count += 1  # Increment the counter

            x_distance = 500 if self.count > 3 else 0  # Determine x position based on count
            y_distance = (165 * (self.count - 4)) if self.count > 3 else (165 * (self.count - 1))  # Determine y position

            Create.frame(
                self.canvas,
                250.0 + x_distance,
                195.0 + y_distance,
                self.image_image_2  # Create a frame for each input field
            )

            Create.label(
                self.canvas,
                136.0 + x_distance,
                173.0 + y_distance,
                key,
                36  # Create a label for the key
            )

            Create.frame(
                self.canvas,
                375.0 + x_distance,
                195.0 + y_distance,
                self.button_image_2,  # Create a frame for the button
            )

            input = Create.input_box(
                290 + x_distance,
                165 + y_distance,
                170,
                60  # Create an input box for user input
            )

            input.insert(0, value)  # Pre-fill the input box with the value

            self.input_data[key] = input  # Store the input box in the dictionary

            Create.frame(
                self.canvas,
                70.0 + x_distance,
                195.0 + y_distance,
                self.image_image_3  # Create a frame for the third image
            )

        Create.label(
            self.canvas,
            340.0,
            46.0,
            f'{data[2]}',
            40  # Create a label for the title
        )

        self.window.mainloop()  # Start the main event loop for the window