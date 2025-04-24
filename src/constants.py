from tkinter import (
    messagebox,
)

# Paths
UTILS_PATH = "src/utils"
ASSETS_PATH = "src/libs/user_interface/assets"

DEVICES_PATH = "src/libs/communicator/devices"
MODEL_PATH = "src/libs/gesture_recognizer/model"
DATASETS_PATH = "src/libs/gesture_recognizer/datasets"

LOGS_PATH = "src/logs"
GESTURE_RECOGNIZER_PATH = "src/libs/gesture_recognizer"

ASSET_PATH = MODEL_PATH + "/gesture_recognizer.task"

# Links
MODEL_LINK = "https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task"
SAMPLES_LINK = "https://storage.googleapis.com/mediapipe-tasks/gesture_recognizer/rps_data_sample.zip"
WEATHER_LINK = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
LOCATION_LINK = "http://ipinfo.io"

# Repository parameters
VERSION = "1.0.0"

# Recognition parameters
MAX_HANDS = 2
MIN_DETECTION_CONFIDENCE = 0.5
MIN_TRACKING_CONFIDENCE = 0.5

# Communication parameters
LOCAL_PORT = 8888
BUFFER_SIZE = 1024

DEFAULT_COMMAND = "successful"

# Training parameters
MIN_ACCURACY_PERCENTAGE = 70
MAX_ACCURACY_PERCENTAGE = 100

# Camera parameters
CAMERA_INDEX = 0
INIT_DELAY = 5  # Seconds
UPDATE_DELAY = 1000  # Milliseconds

# Image parameters
FLIP_CODE = 1
MAX_IMAGES = 100

# Gesture parameters
MIN_GESTURE_NAME_LENGTH = 3
MAX_GESTURE_NAME_LENGTH = 10

# Logger parameters
LOGGING_FORMAT = "%(name)s %(asctime)s %(levelname)s:  %(message)s"
OLD_SIGNATURE = "$"
NEW_SIGNATURE = "\n    "

# Datasets parameters
MIN_GESTURES_AMOUNT = 2

DEFAULT_GESTURE = "None"
NO_GESTURE = "none"

# User interface parameters
WEEKDAYS = [
    "Пн",
    "Вт",
    "Ср",
    "Чт",
    "Пт",
    "Сб",
    "Вс",
]

BOXES_TYPES = [
    messagebox.showinfo,
    messagebox.showwarning,
    messagebox.askyesno,
    messagebox.showerror,
]

DEFAULT_WIN_NAME = "tk"
DEFAULT_WIN_INDEX = 0

TIME_UPDATE_DELAY = 30 * 1000  # Seconds * Milliseconds
DATE_AND_WEATHER_UPDATE_DELAY = 60 * 1000  # Seconds * Milliseconds

# Zone parameters
TIME_FORMAT = "%H:%M"
NO_TEMPERATURE = "~~"
