from tkinter import Tk
from src.constants import *

def accuracy(value: int) -> int:
    # Calculate the accuracy based on the provided value and maximum accuracy percentage
    return round(value * MAX_ACCURACY_PERCENTAGE)

def screen_center(window: Tk, size_x: float, size_y: float) -> tuple[int, int]:
    # Calculate the center position for the window based on screen dimensions and window size
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (size_x / 2)
    y = (screen_height / 2) - (size_y / 2)

    return int(x), int(y)