from tkinter import *

import numpy

from src.constants import *
from src.utils.calculate import screen_center

class Create:
    @staticmethod
    def window(width: int, height: int) -> Tk:
        window = Tk()  # Create a new Tkinter window instance

        x, y = screen_center(window, width, height)  # Calculate the center position for the window

        window.geometry(f'{width}x{height}+{x}+{y}')  # Set the window size and position
        window.resizable(False, False)  # Disable window resizing
       #window.overrideredirect(True)  # Remove window decorations (title bar, etc.)

        window.focus_force()  # Force focus on the window

        return window  # Return the created window instance

    @staticmethod
    def canvas(window, height: float, width: float) -> Canvas:
        canvas = Canvas(
            window,
            bg="#FFFFFF",  # Set background color to white
            height=height,
            width=width,
            bd=0,  # No border
            highlightthickness=0,  # No highlight thickness
            relief="ridge"  # Set relief style to ridge
        )

        canvas.place(x=0, y=0)  # Place the canvas in the top-left corner of the window

        return canvas  # Return the created canvas instance

    @staticmethod
    def label(canvas, x: float, y: float, text: str, point: int) -> Label:
         label = canvas.create_text(
            x,
            y,
            anchor="nw",  # Anchor the text to the northwest (top-left)
            text=text,
            fill="#FFFFFF",  # Set text color to white
            font=("Inter Bold", point * -1)  # Set font style and size
         )

         return label  # Return the created label instance

    @staticmethod
    def image(index: int, image: str) -> Image:
        image_path = ASSETS_PATH + f'/frame{index}/{image}.png'  # Construct the image path

        if Path.exists(image_path):  # Check if the image file exists
            return PhotoImage(
                file=image_path  # Return the PhotoImage instance if the file exists
            )

    @staticmethod
    def frame(canvas, x: float, y: float, image: Image) -> Frame:
        frame = canvas.create_image(
            x,
            y,
            image=image  # Create an image frame on the canvas
        )

        return frame  # Return the created frame instance

    @staticmethod
    def button(image, x: float, y: float, w: float, h: float, callback=None, text=None) -> Button:
        button = Button(
            image=image,
            borderwidth=0,  # No border width
            highlightthickness=0,  # No highlight thickness
            relief="flat",  # Set relief style to flat
            command=callback,  # Set the button's command callback
            text=text,  # Set the button's text
        )

        button.place(
            x=x,
            y=y,
            width=w,
            height=h  # Place the button at specified coordinates with given dimensions
        )

        return button  # Return the created button instance

    @staticmethod
    def box(category: int, title: str, text: str) -> str:
        dialogue_box = BOXES_TYPES[category]  # Get the dialogue box type based on category

        if dialogue_box is not None:  # Check if the dialogue box type is valid
            box = dialogue_box(
                title,
                text  # Create the dialogue box with title and text
            )

            return box  # Return the created box instance

    @staticmethod
    def input_box(x: float, y: float, width: float, height: float) -> Entry:
        input = Entry(
            bd=0,  # No border
            bg="#404040",  # Set background color to dark gray
            fg="#FFFFFF",  # Set text color to white
            highlightthickness=0,  # No highlight thickness
            font=('Inter Bold', 30)  # Set font style and size
        )

        input.place(
            x=x,
            y=y,
            width=width,
            height=height,  # Place the input box at specified coordinates with given dimensions
        )

        return input  # Return the created input box instance