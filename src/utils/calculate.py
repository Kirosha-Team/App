import cv2

from src.constants import MAX_ACCURACY_PERCENTAGE

def frame_timestamp(video_capture: cv2.VideoCapture):
    # Get the current timestamp of the video in milliseconds
    return int(video_capture.get(cv2.CAP_PROP_POS_MSEC))

def accuracy(value: int):
    # Calculate the accuracy based on the provided value and maximum accuracy percentage
    return round(value * MAX_ACCURACY_PERCENTAGE)

def screen_center(window, size_x: float, size_y: float):
    # Calculate the center position for the window based on screen dimensions and window size
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width / 2) - (size_x / 2)
    y = (screen_height / 2) - (size_y / 2)

    return int(x), int(y)