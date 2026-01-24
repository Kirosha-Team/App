"""
NAME: gesture_recognizer.py
DESC: solution for processing given image and calling results

CLASS GESTURE RECOGNIZER:
    PRIVATE METHODS:
        __init__ --> initializes solution
        __result_callback --> calls when process results received

    PUBLIC METHODS:
        process --> callbacks gesture name, image, frame timestamp ms
"""

try:
    import mediapipe

    from mediapipe.tasks import (
        python,
    )
    from mediapipe.tasks.python import (
        vision,
    )
    from mediapipe.tasks.python.vision import (
        RunningMode,
    )
except ImportError:
    raise ImportError("mediapipe is not installed")

from src.utils import *
from src.constants import *


class GestureRecognizer:
    def __init__(
        self,
        listener: callable,
    ):
        if not Path.exists(ASSET_PATH):
            raise OSError("asset directory is empty")

        assert callable(listener)

        model_file = open(
            ASSET_PATH,
            "rb",
        )
        model_data = model_file.read()
        model_file.close()

        self.base_options = python.BaseOptions(model_asset_buffer=model_data)

        self.options = vision.GestureRecognizerOptions(
            base_options=self.base_options,
            running_mode=RunningMode.IMAGE,
        )

        self.recognizer = vision.GestureRecognizer.create_from_options(options=self.options)

        self.listener = listener

    def __result_callback(self, *args) -> None:
        if self.listener:
            gesture = DEFAULT_GESTURE

            results = args[0]

            if results.gestures:
                gesture = results.gestures[0][0].category_name.replace(
                    "\r",
                    "",
                )

            self.listener(gesture)

    def process(
        self,
        image: ndarray,
    ) -> None:
        mp_image = mediapipe.Image(
            image_format=mediapipe.ImageFormat.SRGB,
            data=image,
        )

        result = self.recognizer.recognize(image=mp_image)

        self.__result_callback(result)
