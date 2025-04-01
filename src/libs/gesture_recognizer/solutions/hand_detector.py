"""
    NAME: hand_detector.py
    DESC: solution for processing given image and returning result

    CLASS HAND DETECTOR UTILS:
        STATIC METHODS:
            draw_landmarks --> draws landmarks

    CLASS HAND DETECTOR:
        PRIVATE METHODS:
            __init__ --> initializes util

        PUBLIC METHODS:
            process --> returns hand(s) landmarks
"""
import numpy

from typing import NamedTuple

from mediapipe.python.solutions import hands
from mediapipe.python.solutions import drawing_utils

from src.constants import *

class HandDetectorUtils:
    @staticmethod
    def draw_landmarks(image: numpy.ndarray, multi_hand_landmarks=None) -> None:
        # Check if there are any hand landmarks to draw
        if multi_hand_landmarks:
            # Iterate through each set of hand landmarks
            for hand_landmarks in multi_hand_landmarks:
                # Draw the landmarks on the image with specified connections
                drawing_utils.draw_landmarks(
                    image=image,
                    landmark_list=hand_landmarks,
                    connections=hands.HAND_CONNECTIONS
                )

class HandDetector:
    def __init__(self):
        # Initialize the Hands object with specified parameters
        self.Hands = hands.Hands(
            static_image_mode=False,  # Set to False for dynamic hand tracking
            max_num_hands=MAX_HANDS,  # Maximum number of hands to detect
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE,  # Minimum confidence for tracking
            min_detection_confidence=MIN_DETECTION_CONFIDENCE  # Minimum confidence for detection
        )

    def process(self, image: numpy.ndarray) -> NamedTuple:
        # Process the input image to detect hands
        return self.Hands.process(image)