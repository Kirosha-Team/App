import numpy

from mediapipe.python.solutions import hands
from mediapipe.python.solutions import drawing_utils

def draw(image: numpy.ndarray, multi_hand_landmarks=None):
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