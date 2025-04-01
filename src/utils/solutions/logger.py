import logging

from src.utils.solutions.path import *

from src.constants import *

class LoggerUtils:
    @staticmethod
    def convert(message: str) -> str:
        return f'${message}'.replace('$', '\n    ')

class Logger:
    def __init__(self, name: str):
        # Ensure the name is of type string
        assert(type(name) is str)

        # Create a file handler that writes log messages to a file
        self.handler = handler = logging.FileHandler(
            filename=Path.get_path_to(f'{name}.log', LOGS_PATH),
            mode='w'
        )

        # Create a formatter for log messages with specific formatting
        self.formatter = logging.Formatter(FORMATTER)

        # Set the formatter for the handler to define the log message format
        self.handler.setFormatter(self.formatter)

        # Create a logger with the specified name and set its logging level
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # Add the file handler to the logger
        self.logger.addHandler(handler)

    def assertion(self, value: bool, message: str) -> None:
        # Log an error message if the assertion fails
        if not value:
            self.logger.error(msg=LoggerUtils.convert(message))

    def error(self, message: str) -> None:
        # Log an error message
        self.logger.error(msg=LoggerUtils.convert(message))

    def warning(self, message: str) -> None:
        # Log a warning message
        self.logger.warning(msg=LoggerUtils.convert(message))

    def debug(self, message: str) -> None:
        # Log a debug message
        self.logger.debug(msg=LoggerUtils.convert(message))