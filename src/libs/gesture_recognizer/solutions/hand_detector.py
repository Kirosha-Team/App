"""
NAME: hand_detector.py
DESC: solution for processing given image and returning result

CLASS HAND DETECTOR UTILS:
    STATIC METHODS:
        draw_landmarks --> draws landmarks

CLASS HAND DETECTOR:
    PRIVATE METHODS:
        __init__ --> initializes solution

    PUBLIC METHODS:
        process --> returns hand(s) landmarks
"""

try:
    import numpy

    from typing import (
        NamedTuple,
    )

    from mediapipe.python.solutions import (
        hands,
    )
    from mediapipe.python.solutions import (
        drawing_utils,
    )
except ImportError:
    raise ImportError("mediapipe is not installed")

from src.constants import *


class HandDetectorUtils:
    @staticmethod
    def draw_landmarks(
        image: numpy.ndarray,
        multi_hand_landmarks=None,
    ) -> None:
        if multi_hand_landmarks:
            for hand_landmarks in multi_hand_landmarks:
                drawing_utils.draw_landmarks(
                    image=image,
                    landmark_list=hand_landmarks,
                    connections=hands.HAND_CONNECTIONS,
                )


class HandDetector:
    def __init__(
        self,
    ):
        self.Hands = hands.Hands(
            static_image_mode=False,
            max_num_hands=MAX_HANDS,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
        )

    def process(
        self,
        image: numpy.ndarray,
    ) -> NamedTuple:
        return self.Hands.process(image)
