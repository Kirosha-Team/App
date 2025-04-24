"""
NAME: calculate.py
DESC: solution for calculating variables

PUBLIC METHODS:
    accuracy --> returns rounded input value
    screen_center --> returns X and Y of the display center
"""

from tkinter import (
    Tk,
)
from src.constants import *


def accuracy(
    value: int,
) -> int:
    return round(value * MAX_ACCURACY_PERCENTAGE)


def screen_center(
    window: Tk,
    size_x: float,
    size_y: float,
) -> tuple[
    int,
    int,
]:
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (size_x / 2)
    y = (screen_height / 2) - (size_y / 2)

    return int(x), int(y)
