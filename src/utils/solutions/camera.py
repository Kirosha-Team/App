"""
    NAME: camera.py
    DESC: solution for controlling video capture

    CLASS CAMERA UTILS:
        STATIC METHODS:
            convert --> returns converted from BGR to RGB image
            save --> saves image in .png format
            show --> creates window with image inside
            destroy_all_windows --> destroys all the showing windows

    CLASS CAMERA:
        PRIVATE METHODS:
            __init__ --> initializes solution

        PUBLIC METHODS:
            change --> changes callback function
            start --> runs video capture and callbacks input images
            is_running --> returns video capture state
            stop --> closes video capture
"""

import cv2, numpy

from src.constants import *

class CameraUtils:
    @staticmethod
    def convert(image: numpy.ndarray) -> numpy.ndarray:
        new_image = image.__copy__()
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)

        return new_image

    @staticmethod
    def save(image: numpy.ndarray, name: str, index: int) -> None:
        try:
            cv2.imwrite(
                filename=DATASETS_PATH + f'/{name}/{str(index)}.jpg',
                img=image
            )
        except OSError:
            pass

    @staticmethod
    def show(image: numpy.ndarray) -> None:
        cv2.imshow(DEFAULT_WIN_NAME, image)

    @staticmethod
    def destroy_all_windows() -> None:
        cv2.destroyAllWindows()

class VideoCapture:
    def __init__(self):
        self.capture = None

        self.__running = False
        self.__callback = None

    def change(self, callback: callable) -> None:
        assert(callable(callback))

        self.__callback = callback

    def start(self) -> None:
        assert(callable(self.__callback))

        self.capture = cv2.VideoCapture(CAMERA_INDEX)

        assert(self.capture.isOpened())

        self.__running = True

        while self.capture.isOpened():
            success, frame = self.capture.read()

            cv2.waitKey(
                delay=UPDATE_DELAY
            )

            if not success:
                continue

            self.__callback(cv2.flip(frame, FLIP_CODE))

        self.__running = False

    def is_running(self) -> bool:
        return self.__running is True

    def stop(self) -> None:
        self.capture.release()