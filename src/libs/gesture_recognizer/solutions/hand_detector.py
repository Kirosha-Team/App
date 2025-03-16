"""
    NAME: hand_detector.py

    DESC: solution for processing given image and returning result

    PRIVATE METHODS:
        __init__ --> initializes util

    PUBLIC METHODS:
        process --> returns hand(s) landmarks
"""

import numpy

from mediapipe.python.solutions import hands

from src.constants import (
    MIN_TRACKING_CONFIDENCE,
    MIN_DETECTION_CONFIDENCE,
    MAX_HANDS
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

    def process(self, image: numpy.ndarray):
        # Process the input image to detect hands
        return self.Hands.process(image)