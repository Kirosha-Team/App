import time, datetime

from src.constants import *
from src.utils import *

class MainMenu:
    def __init__(self, on_button_pressed: callable, on_display_info_pressed: callable):
        self.callback = on_button_pressed  # Store the callback function for button press
        self.display = on_display_info_pressed  # Store the callback function for display info

        self.time = None  # Initialize time variable
        self.date = None  # Initialize date variable
        self.weather = None  # Initialize weather variable

    def create(self) -> None:
        self.window = Create.window(1000, 600)  # Create a window with specified dimensions
        self.canvas = Create.canvas(self.window, 600, 1000)  # Create a canvas within the window

        self.image_image_1 = Create.image(0, "image_1")  # Load the first image
        self.image_image_2 = Create.image(0, "image_2")  # Load the second image
        self.button_image_1 = Create.image(0, "button_1")  # Load the first button image
        self.button_image_2 = Create.image(0, "button_2")  # Load the second button image
        self.button_image_3 = Create.image(0, "button_3")  # Load the third button image

        def update() -> None:
            current_time = time.strftime('%H:%M')  # Get the current time in HH:MM format

            date = datetime.date.today()  # Get today's date
            weekday = WEEKDAYS[datetime.date.weekday(date)]  # Get the current weekday

            self.canvas.itemconfig(tagOrId=self.time, text=current_time)  # Update the time label on the canvas
            self.canvas.itemconfig(tagOrId=self.date, text=f'{weekday}.\n{date.day}')  # Update the date label on the canvas

            self.window.after(UPDATE_DELAY, update)  # Schedule the update function to run again after a delay

        Create.frame(
            self.canvas,
            500.0,
            300.0,
            self.image_image_1  # Create a frame with the first image
        )

        Create.frame(
            self.canvas,
            335.0,
            520.0,
            self.image_image_2  # Create a frame with the second image
        )

        Create.button(
            self.button_image_1,
            475.0,
            475.0,
            90.0,
            90.0,
            lambda: self.callback(1, False, False)  # Set up button 1 to call the callback with specific parameters
        )

        Create.button(
            self.button_image_2,
            585.0,
            475.0,
            90.0,
            90.0,
            lambda: self.callback(2, False, False)  # Set up button 2 to call the callback with specific parameters
        )

        Create.button(
            self.button_image_3,
            695.0,
            475.0,
            90.0,
            90.0,
            lambda: self.display()  # Set up button 3 to call the display function
        )

        self.time = Create.label(
            self.canvas,
            313.0,
            63.0,
            '',
            128  # Create a label for displaying time
        )

        self.date = Create.label(
            self.canvas,
            253.0,
            486.0,
            '',
            28  # Create a label for displaying date
        )

        self.weather = Create.label(
            self.canvas,
            364.0,
            503.0,
            '~~°C',
            28  # Create a label for displaying weather
        )

        update()  # Call the update function to start the time and date updates

        self.window.mainloop()  # Start the main event loop of the window