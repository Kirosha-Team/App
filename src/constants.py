from tkinter import messagebox

from src.utils.path import Path

# Application configuration
VERSION = '1.00.0'  # Current version of the application

# Defining paths for various resources
UTILS_PATH = 'src/utils'  # Path to utility functions
ASSETS_PATH = 'src/libs/user_interface/assets'  # Path to user interface assets

DEVICES_PATH = 'src/libs/communicator/devices'  # Path to device communication resources
MODEL_PATH = 'src/libs/gesture_recognizer/model'  # Path to gesture recognition model
DATASETS_PATH = 'src/libs/gesture_recognizer/datasets'  # Path to datasets for gesture recognition

LOGS_PATH = 'src/logs' # Path to logs
GESTURE_RECOGNIZER_PATH = 'src/libs/gesture_recognizer' # Path to gesture recognizer library

# Getting the asset path for the gesture recognizer model
ASSET_PATH = Path.get_path_to('gesture_recognizer.task', MODEL_PATH)  # Fetching the model path using Path utility

# Links to the model and sample data
MODEL_LINK = 'https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task'  # URL for the gesture recognizer model
SAMPLES_LINK = 'https://storage.googleapis.com/mediapipe-tasks/gesture_recognizer/rps_data_sample.zip'  # URL for sample data

# Configuration constants for gesture recognition
MAX_HANDS = 2  # Maximum number of hands to detect
MIN_DETECTION_CONFIDENCE = 0.5  # Minimum confidence for detection to be considered valid
MIN_TRACKING_CONFIDENCE = 0.5  # Minimum confidence for tracking to be considered valid

# Accuracy thresholds
MIN_ACCURACY_PERCENTAGE = 70  # Minimum accuracy percentage for valid recognition
MAX_ACCURACY_PERCENTAGE = 100  # Maximum accuracy percentage

# Image configuration
FLIP_CODE = 1 # Image rotation code
MAX_IMAGES = 100  # Maximum number of images to save

# Datasets configuration
MIN_GESTURES_AMOUNT = 2 # Default datasets directory size
DEFAULT_GESTURE = 'None'  # Default gesture when None gesture is recognized

# Gesture configuration
NO_GESTURE = 'none'  # Default gesture when no gesture is recognized

# Communication configuration
DEFAULT_COMMAND = 'ps'

# Networking configuration
LOCAL_PORT = 8888  # Port for local communication
BUFFER_SIZE = 1024  # Buffer size for data transmission

# Camera configuration
CAMERA_INDEX = 0 # Current camera
INIT_DELAY = 5 # Delay for camera initialization in seconds
UPDATE_DELAY = 1  # Delay for updates in milliseconds

# Menu configuration
WEEKDAYS = ['Пн', 'Вт', 'Ср', 'Чт','Пт', 'Сб', 'Вс',]  # List of weekdays in Russian

# Types of message boxes for user notifications
BOXES_TYPES = [messagebox.showinfo, messagebox.showwarning, messagebox.askyesno, messagebox.showerror]  # Different types of message boxes available

# Window configuration
DEFAULT_WIN_NAME = "Tk" # Default name of the window
DEFAULT_WIN_INDEX = 0 # Default window to open

# Gesture configuration
MIN_GESTURE_NAME_LENGTH = 3
MAX_GESTURE_NAME_LENGTH = 10

# Logger configuration
FORMAT = "%(name)s %(asctime)s %(levelname)s:  %(message)s"