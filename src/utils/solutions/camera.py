"""
NAME: camera.py
DESC: solution for controlling video capture

CLASS CAMERA UTILS:
    STATIC METHODS:
        convert --> returns converted from BGR to RGB image
        save --> saves image in .png format
        show --> creates window with image inside
        destroy_all_windows --> destroys all the showing windows

CLASS CAMERA CAPTURE:
    PRIVATE METHODS:
        __init__ --> initializes solution

    PUBLIC METHODS:
        change --> changes callback function
        start --> runs video capture and callbacks input images
        stop --> closes video capture
        is_running --> returns video capture state
        destroy --> destroys video capture

SUB-CLASS USB INTERFACE:
    DESC: class for controlling USB camera

SUB-CLASS CLI INTERFACE:
    DESC: class for controlling CLI camera
"""

from threading import (
    Thread,
)

try:
    from numpy import ndarray, rot90
    from cv2 import cvtColor, COLOR_BGR2RGB, imwrite, imshow, destroyAllWindows, VideoCapture, flip, waitKey
except ImportError:
    raise ImportError("cv2 is not installed")

try:
    from picamera2 import Picamera
except ImportError:
    pass

from src.constants import *


class CameraUtils:
    @staticmethod
    def convert(
        image: ndarray,
    ) -> ndarray:
        new_image = image.__copy__()
        new_image = cvtColor(
            new_image,
            COLOR_BGR2RGB,
        )

        return new_image

    @staticmethod
    def save(
        image: ndarray,
        name: str,
        index: int,
    ) -> None:
        try:
            imwrite(
                filename=DATASETS_PATH + f"/{name}/{str(index)}.jpg",
                img=image,
            )
        except OSError:
            pass

    @staticmethod
    def show(
        image: ndarray,
    ) -> None:
        imshow(
            DEFAULT_WIN_NAME,
            image,
        )

    @staticmethod
    def destroy_all_windows() -> None:
        destroyAllWindows()


class CameraCapture:
    def __init__(
        self,
    ):
        self.capture = None
        self.thread = None

        self.running = False
        self.callback = None

    def change(
        self,
        callback: callable,
    ):
        raise NotImplementedError("change method must be called in sub-classes")

    def start(
        self,
    ):
        raise NotImplementedError("start method must be called in sub-classes")

    def stop(
        self,
    ):
        raise NotImplementedError("stop method must be called in sub-classes")

    def running(
        self,
    ):
        raise NotImplementedError("is_running method must be called in sub-classes")

    def destroy(
        self,
    ):
        raise NotImplementedError("destroy method must be called in sub-classes")


class UsbInterface(CameraCapture):
    def __init__(
        self,
    ):
        super().__init__()

        self.capture = VideoCapture(CAMERA_INDEX)

        assert self.capture.isOpened()

        def __run():
            while self.capture.isOpened():
                if self.running is False:
                    continue

                if self.callback is None:
                    continue

                (
                    success,
                    frame,
                ) = self.capture.read()

                if not success:
                    continue

                self.callback(
                    flip(
                        frame,
                        FLIP_CODE,
                    )
                )

                waitKey(delay=UPDATE_DELAY)

        self.thread = Thread(target=__run)
        self.thread.start()

    def change(
        self,
        callback: callable,
    ) -> None:
        assert callable(callback)

        self.callback = callback

    def start(
        self,
    ) -> None:
        self.running = True

    def stop(
        self,
    ) -> None:
        self.running = False

    def is_running(
        self,
    ) -> bool:
        return self.running is True

    def destroy(
        self,
    ) -> None:
        self.capture.release()


class CliInterface(CameraCapture):
    def __init__(
        self,
    ):
        super().__init__()

        self.capture = Picamera()
        self.capture.start()

        assert self.capture.is_open

        def __run():
            while self.capture.is_open:
                if self.running is False:
                    continue

                if self.callback is None:
                    continue

                (frame) = self.capture.capture_array()
                (frame) = CameraUtils.convert(frame)
                (frame) = rot90(
                    frame,
                    k=-1,
                )

                self.callback(frame)

        self.thread = Thread(target=__run)
        self.thread.start()

    def change(
        self,
        callback: callable,
    ) -> None:
        assert callable(callback)

        self.callback = callback

    def start(
        self,
    ) -> None:
        self.running = True

    def stop(
        self,
    ) -> None:
        self.running = False

    def is_running(
        self,
    ) -> bool:
        return self.running is True

    def destroy(
        self,
    ) -> None:
        self.capture.stop()
