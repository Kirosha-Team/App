from tkinter import messagebox

from src.utils.path import Path

# Defining paths for various resources
UTILS_PATH = 'src/utils'  # Path to utility functions
ASSETS_PATH = 'src/libs/user_interface/assets'  # Path to user interface assets

DEVICES_PATH = 'src/libs/communicator/devices'  # Path to device communication resources
MODEL_PATH = 'src/libs/gesture_recognizer/model'  # Path to gesture recognition model
DATASETS_PATH = 'src/libs/gesture_recognizer/datasets'  # Path to datasets for gesture recognition

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

NO_GESTURE = 'none'  # Default gesture when no gesture is recognized
DEFAULT_GESTURE = 'None'  # Default gesture when None gesture is recognized

# Networking configuration
LOCAL_PORT = 8888  # Port for local communication
BUFFER_SIZE = 1024  # Buffer size for data transmission

UPDATE_DELAY = 1000  # Delay for updates in milliseconds
WEEKDAYS = ['Пн', 'Вт', 'Ср', 'Чт','Пт', 'Сб', 'Вс',]  # List of weekdays in Russian

# Types of message boxes for user notifications
BOXES_TYPES = [messagebox.showinfo, messagebox.showwarning, messagebox.askyesno, messagebox.showerror]  # Different types of message boxes available

VERSION = '0.00.1'  # Current version of the application
MAX_IMAGES = 100  # Maximum number of images to process