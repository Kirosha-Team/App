"""
    NAME: gesture_recognizer.py

    DESC: solution for processing given image and calling results

    PRIVATE METHODS:
        __init__ --> initializes util
        __result_callback --> calls when process results received

    PUBLIC METHODS:
        process --> callbacks gesture name, image, frame timestamp ms
"""

import mediapipe, numpy

from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.vision import RunningMode

from src.constants import *

class GestureRecognizer:
    def __result_callback(self, *args) -> None:
        if self.listener:  # Check if a listener is set
            gesture = DEFAULT_GESTURE  # Default gesture if none detected

            results = args[0]  # Get the results from the callback arguments

            if results.gestures:  # Check if any gestures were detected
                gesture = results.gestures[0][0].category_name.replace('\r', '')  # Extract the gesture name

            self.listener(gesture)  # Notify the listener with the detected gesture

    def __init__(self, listener: callable):
        if not Path.exists(ASSET_PATH):  # Ensure the asset path exists
            print(f'[ERROR]: gesture_recognizer.task nil or missing!')
            return

        assert (callable(listener))  # Ensure the listener is a callable function

        model_file = open(ASSET_PATH, "rb")  # Open the model file in binary read mode
        model_data = model_file.read()  # Read the model data
        model_file.close()  # Close the model file

        self.base_options = python.BaseOptions(
            model_asset_buffer=model_data  # Set the model data as buffer
        )

        self.options = vision.GestureRecognizerOptions(
            base_options=self.base_options,
            running_mode=RunningMode.IMAGE,  # Set the running mode to live stream
        )

        self.recognizer = vision.GestureRecognizer.create_from_options(
            options=self.options  # Create the recognizer with the specified options
        )

        self.listener = listener  # Assign the listener to the instance variable

    def process(self, image: numpy.ndarray) -> None:
        mp_image = mediapipe.Image(
            image_format=mediapipe.ImageFormat.SRGB,  # Set the image format to SRGB
            data=image  # Assign the image data
        )

        result = self.recognizer.recognize(
            image=mp_image,  # Pass the image to the recognizer
        )

        self.__result_callback(result) # Send results to get the top gesture