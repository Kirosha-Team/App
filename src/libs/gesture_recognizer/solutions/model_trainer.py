"""
    NAME: model_trainer.py

    DESC: solution for creating gesture recognition model

    PRIVATE METHODS:
        __init__ -> initializes util

    PUBLIC METHODS:
        train -> returns model
        get_accuracy -> tests model to get accuracy and loss
        export -> creates a new model
"""

from mediapipe_model_maker import gesture_recognizer

from src.constants import *

class ModelTrainer:
    def __init__(self):
        # Check if the datasets directory is empty and warn the user if it is
        if Path.empty(DATASETS_PATH):
            print(f'[WARNING]: datasets directory is empty. Required 1 or more gestures')
            return

        # Load dataset from the specified folder with preprocessing parameters
        self.data = gesture_recognizer.Dataset.from_folder(
            dirname=DATASETS_PATH,
            hparams=gesture_recognizer.HandDataPreprocessingParams()
        )

        # Set hyperparameters for the model export directory
        self.hparams = gesture_recognizer.HParams(
            export_dir=MODEL_PATH
        )

        # Initialize gesture recognizer options with the hyperparameters
        self.options = gesture_recognizer.GestureRecognizerOptions(
            hparams=self.hparams
        )

        self.model = None
        self.test_data = None
        self.train_data = None

    def train(self) -> None:
        # Clean the model directory before training
        Path.clean_directory(MODEL_PATH)

        # Split the dataset into training and testing data
        self.train_data, remaining_data = self.data.split(0.8)
        self.test_data, validation_data = remaining_data.split(0.5)

        # Create the gesture recognizer model with training and validation data
        self.model = gesture_recognizer.GestureRecognizer.create(
            train_data=self.train_data,
            validation_data=validation_data,
            options=self.options,
        )

    def get_accuracy(self) -> tuple[int, int]:
        # Ensure the model is trained before evaluating accuracy
        assert (self.model is not None)

        # Evaluate the model's accuracy on the test data
        return self.model.evaluate(self.test_data, batch_size=1)

    def export(self) -> None:
        # Ensure the model is trained before exporting
        assert (self.model is not None)

        # Export the trained model
        self.model.export_model()
