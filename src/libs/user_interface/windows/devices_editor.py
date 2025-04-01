from src.libs.communicator import *
from src.utils import *

class DevicesEditor:
    def __init__(self, on_button_pressed: callable):
        self.callback = on_button_pressed  # Store the callback function for button presses
        self.registry = Registry()  # Initialize the registry to manage devices

    def create(self) -> None:
        self.window = Create.window(1000, 600)  # Create a window with specified dimensions
        self.canvas = Create.canvas(self.window, 600, 1000)  # Create a canvas within the window

        self.image_image_1 = Create.image(1, "image_1")  # Load the first image
        self.image_image_2 = Create.image(1, "image_2")  # Load the second image
        self.image_image_3 = Create.image(1, "image_3")  # Load the third image
        self.button_image_1 = Create.image(1, "button_1")  # Load the first button image
        self.button_image_2 = Create.image(1, "button_2")  # Load the second button image
        self.button_image_3 = Create.image(1, "button_3")  # Load the third button image
        self.button_image_4 = Create.image(1, "button_4")  # Load the fourth button image

        self.count = 0  # Initialize a counter for device placement
        self.devices = Registry.get_devices() or []  # Retrieve devices from the registry or set to empty list

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
            lambda: self.callback(0)  # Set up a button that triggers the callback with a specific argument
        )

        Create.label(
            self.canvas,
            300.0,
            46.0,
            'Управление устройствами',  # Create a label on the canvas with the specified text
            40
        )

        for data in self.devices:
            name = data[2]  # Extract the device name from the data

            self.count += 1  # Increment the device counter

            x_distance = 500 if self.count > 3 else 0  # Determine x position based on count
            y_distance = (165 * (self.count - 4)) if self.count > 3 else (165 * (self.count - 1))  # Determine y position based on count

            Create.frame(
                self.canvas,
                250.0 + x_distance,
                195.0 + y_distance,
                self.image_image_2  # Create a frame for each device on the canvas
            )

            Create.label(
                self.canvas,
                136.0 + x_distance,
                173.0 + y_distance,
                name,  # Create a label for the device name
                36
            )

            Create.button(
                self.button_image_4,
                285.0 + x_distance,
                160.0 + y_distance,
                180.0,
                70.0,
                lambda device=data: self.callback(4, False, False, device)  # Set up a button for each device that triggers the callback with device data
            )

            Create.frame(
                self.canvas,
                70.0 + x_distance,
                195.0 + y_distance,
                self.image_image_3  # Create another frame for the device on the canvas
            )

        self.window.mainloop()  # Start the main event loop for the window