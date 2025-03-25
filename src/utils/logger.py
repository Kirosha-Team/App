import logging

from src.constants import *

# Create a formatter for log messages with specific formatting
formatter = logging.Formatter(FORMAT)

class Logger:
    @staticmethod
    def __convert(message: str):
        return f'${message}'.replace('$', '\n    ')

    def __init__(self, name: str):
        # Ensure the name is of type string
        assert(type(name) is str)

        # Create a file handler that writes log messages to a file
        self.handler = handler = logging.FileHandler(
            filename=Path.get_path_to(f'{name}.log', LOGS_PATH),
            mode='w'
        )

        # Set the formatter for the handler to define the log message format
        self.handler.setFormatter(formatter)

        # Create a logger with the specified name and set its logging level
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # Add the file handler to the logger
        self.logger.addHandler(handler)

    def assertion(self, value: bool, message: str) -> None:
        # Log an error message if the assertion fails
        if not value:
            self.logger.error(msg=self.__convert(message))

    def error(self, message: str) -> None:
        # Log an error message
        self.logger.error(msg=self.__convert(message))

    def warning(self, message: str) -> None:
        # Log a warning message
        self.logger.warning(msg=self.__convert(message))

    def debug(self, message: str) -> None:
        # Log a debug message
        self.logger.debug(msg=self.__convert(message))