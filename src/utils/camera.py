import cv2, numpy

from src.constants import (
    DATASETS_PATH
)

class VideoCapture:
    def __init__(self):
        self.capture = None  # Initialize capture variable to None

        self.__delay = 1 # Set delay value to 1
        self.__running = False  # Set running state to False
        self.__callback = None  # Set callback value to None

    @staticmethod
    def save(image: numpy.ndarray, name: str, index: int):
        try:
            # Attempt to write the image to the specified path
            cv2.imwrite(
                filename=DATASETS_PATH + f'/{name}/{str(index)}.jpg',
                # Construct the file path using the dataset path, name, and index
                img=image  # The image to be saved
            )
        except OSError:
            # Print an error message if the image cannot be saved
            print(f'[ERROR]: unable to save {name} image')

    def change(self, callback, delay=1):
        assert(type(delay) == int)  # Ensure delay_value is a integer
        assert(callable(callback))  # Ensure image_changed is a callable function

        self.__callback = callback
        self.__delay = delay

    def start(self):
        assert(callable(self.__callback)) # Ensure callback is a callable function

        self.capture = cv2.VideoCapture(0)  # Start video capture from the default camera

        assert(self.capture.isOpened()) # Ensure capture is opened

        self.__running = True  # Set running state to True

        while self.capture.isOpened():  # Loop while the camera is open
            success, frame = self.capture.read()  # Read a frame from the camera

            # Pause execution for the specified delay
            cv2.waitKey(
                delay=self.__delay
            )

            if not success:  # If frame reading was unsuccessful
                continue  # Skip to the next iteration

            self.__callback(cv2.flip(frame, 1))  # Call the image_changed function with the flipped frame

        self.__running = False  # Set running state to False when the loop ends

    def is_running(self):
        return self.__running is True  # Return True if the capture is running

    def stop(self):
        self.capture.release()  # Release the video capture resources
        cv2.destroyAllWindows()