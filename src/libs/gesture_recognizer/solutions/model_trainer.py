"""
NAME: model_trainer.py

DESC: solution for creating gesture recognition model

CLASS MODEL TRAINER:
    PRIVATE METHODS:
        __init__ --> initializes solution

    PUBLIC METHODS:
        train --> returns model
        get_accuracy --> tests model to get accuracy and loss
        export --> creates a new model
"""

try:
    from mediapipe_model_maker import (
        gesture_recognizer,
    )
except ImportError:
    raise ImportError(
        "mediapipe-model-maker is not installed"
    )

from src.utils import *
from src.constants import *


class ModelTrainer:
    def __init__(
        self,
    ):
        if Path.empty(
            DATASETS_PATH
        ):
            raise OSError(
                "datasets directory is empty or missing"
            )

        if not Path.exists(
            Path.get_path_to(
                "None",
                DATASETS_PATH,
            )
        ) or not Path.exists(
            Path.get_path_to(
                "none",
                DATASETS_PATH,
            )
        ):
            raise OSError(
                "none gesture is missing"
            )

        self.data = gesture_recognizer.Dataset.from_folder(
            dirname=DATASETS_PATH,
            hparams=gesture_recognizer.HandDataPreprocessingParams(),
        )

        self.hparams = gesture_recognizer.HParams(
            export_dir=MODEL_PATH
        )

        self.options = gesture_recognizer.GestureRecognizerOptions(
            hparams=self.hparams
        )

        self.model = None
        self.test_data = None
        self.train_data = None

    def train(
        self,
    ) -> None:
        Path.clean_directory(
            MODEL_PATH
        )

        (
            self.train_data,
            remaining_data,
        ) = self.data.split(
            0.8
        )
        (
            self.test_data,
            validation_data,
        ) = remaining_data.split(
            0.5
        )

        self.model = gesture_recognizer.GestureRecognizer.create(
            train_data=self.train_data,
            validation_data=validation_data,
            options=self.options,
        )

    def get_accuracy(
        self,
    ) -> tuple[
        int,
        int,
    ]:
        assert (
            self.model
            is not None
        )

        return self.model.evaluate(
            self.test_data,
            batch_size=1,
        )

    def export(
        self,
    ) -> None:
        assert (
            self.model
            is not None
        )

        self.model.export_model()
