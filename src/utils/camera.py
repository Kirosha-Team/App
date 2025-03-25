import cv2, numpy

from src.constants import *

class Utils:
    @staticmethod
    def convert(image: numpy.ndarray) -> numpy.ndarray:
        new_image = image.__copy__() # Copy the existing image
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB) # Convert color from BGR to RGB

        return new_image # Return the converted image

    @staticmethod
    def save(image: numpy.ndarray, name: str, index: int) -> None:
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

    @staticmethod
    def show(image: numpy.ndarray) -> None:
        cv2.imshow(DEFAULT_WIN_NAME, image) # Display image in the window

    @staticmethod
    def destroy_all_windows() -> None:
        cv2.destroyAllWindows() # Destroy existing windows

class VideoCapture:
    def __init__(self):
        self.capture = None  # Initialize capture variable to None

        self.__running = False  # Set running state to False
        self.__callback = None  # Set callback value to None

    def change(self, callback: callable) -> None:
        assert(callable(callback))  # Ensure image_changed is a callable function

        self.__callback = callback

    def start(self) -> None:
        assert(callable(self.__callback)) # Ensure callback is a callable function

        self.capture = cv2.VideoCapture(CAMERA_INDEX)  # Start video capture from the default camera

        assert(self.capture.isOpened()) # Ensure capture is opened

        self.__running = True  # Set running state to True

        while self.capture.isOpened():  # Loop while the camera is open
            success, frame = self.capture.read()  # Read a frame from the camera

            # Pause execution for the specified delay
            cv2.waitKey(
                delay=UPDATE_DELAY
            )

            if not success:  # If frame reading was unsuccessful
                continue  # Skip to the next iteration

            self.__callback(cv2.flip(frame, FLIP_CODE))  # Call the image_changed function with the flipped frame

        self.__running = False  # Set running state to False when the loop ends

    def is_running(self) -> bool:
        return self.__running is True  # Return True if the capture is running

    def stop(self) -> None:
        self.capture.release()  # Release the video capture resources