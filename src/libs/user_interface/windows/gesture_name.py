from src.utils.create import Create

class GestureName:
    def __init__(self, on_button_pressed: callable, on_save_pressed: callable):
        self.save = on_save_pressed  # Assign the save callback function to an instance variable
        self.callback = on_button_pressed  # Assign the button pressed callback function to an instance variable

    def create(self) -> None:
        self.window = Create.window(400, 250)  # Create a window with specified dimensions
        self.canvas = Create.canvas(self.window, 250, 400)  # Create a canvas within the window

        self.image_image_1 = Create.image(2, "image_1")  # Load the first image
        self.button_image_1 = Create.image(2, "button_1")  # Load the first button image
        self.button_image_2 = Create.image(2, "button_2")  # Load the second button image

        Create.frame(
            self.canvas,
            200.0,
            125.0,
            self.image_image_1  # Create a frame on the canvas with the first image
        )

        Create.button(
            self.button_image_1,
            10.0,
            170.0,
            180.0,
            70.0,
            lambda: self.save(self.entry.get())  # Set up a button that calls the save function with the entry text
        )

        Create.button(
            self.button_image_2,
            210.0,
            170.0,
            180.0,
            70.0,
            lambda: self.callback(1, False, False)  # Set up a button that calls the callback function with a fixed argument
        )

        self.entry = Create.input_box(
            15.0,
            70.0,
            370.0,
            68.0  # Create an input box for user text input
        )

        self.window.mainloop()  # Start the main event loop for the window