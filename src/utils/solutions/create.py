"""
NAME: create.py
DESC: solution for managing ui components

CLASS CREATE:
    STATIC METHODS:
        window --> returns window
        canvas --> returns canvas
        label --> creates text inside canvas
        image --> loads image from assets
        frame --> creates image inside canvas
        button --> creates button
        box --> creates dialogue box
        input_box --> creates entry
"""

from tkinter import *

from src.utils.solutions.calculate import *
from src.utils.solutions.path import *
from src.constants import *


class Create:
    @staticmethod
    def window(
        width: int,
        height: int,
    ) -> (
        Tk
    ):
        window = (
            Tk()
        )

        (
            x,
            y,
        ) = screen_center(
            window,
            width,
            height,
        )

        window.geometry(
            f"{width}x{height}+{x}+{y}"
        )
        window.resizable(
            False,
            False,
        )
        # window.overrideredirect(True)

        window.focus_force()

        return window

    @staticmethod
    def canvas(
        window: Tk,
        height: float,
        width: float,
    ) -> Canvas:
        canvas = Canvas(
            window,
            bg="#FFFFFF",
            height=height,
            width=width,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        canvas.place(
            x=0,
            y=0,
        )

        return canvas

    @staticmethod
    def label(
        canvas: Canvas,
        x: float,
        y: float,
        text: str,
        point: int,
    ) -> int:
        label = canvas.create_text(
            x,
            y,
            anchor="nw",
            text=text,
            fill="#FFFFFF",
            font=(
                "Inter Bold",
                point
                * -1,
            ),
        )

        return label

    @staticmethod
    def image(
        index: int,
        image: str,
    ) -> Image:
        image_path = (
            ASSETS_PATH
            + f"/frame{index}/{image}.png"
        )

        if Path.exists(
            image_path
        ):
            return PhotoImage(
                file=image_path
            )

    @staticmethod
    def frame(
        canvas: Canvas,
        x: float,
        y: float,
        image: Image,
    ) -> int:
        frame = canvas.create_image(
            x,
            y,
            image=image,
        )

        return frame

    @staticmethod
    def button(
        image: Image,
        x: float,
        y: float,
        w: float,
        h: float,
        callback=None,
        text=None,
    ) -> Button:
        button = Button(
            image=image,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=callback,
            text=text,
        )

        button.place(
            x=x,
            y=y,
            width=w,
            height=h,
        )

        return button

    @staticmethod
    def box(
        category: int,
        title: str,
        text: str,
    ) -> str:
        dialogue_box = BOXES_TYPES[
            category
        ]

        if (
            dialogue_box
            is not None
        ):
            box = dialogue_box(
                title,
                text,
            )

            return box

    @staticmethod
    def input_box(
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> Entry:
        entry = Entry(
            bd=0,
            bg="#404040",
            fg="#FFFFFF",
            highlightthickness=0,
            font=(
                "Inter Bold",
                30,
            ),
        )

        entry.place(
            x=x,
            y=y,
            width=width,
            height=height,
        )

        return entry
