import logging

# Create a formatter for log messages with specific formatting
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s:  %(message)s")

class Logger:
    def __init__(self, name: str):
        # Ensure the name is of type string
        assert(type(name) is str)

        # Create a file handler that writes log messages to a file
        self.handler = handler = logging.FileHandler(
            filename=f'{name}.log',
            mode='w'
        )

        # Set the formatter for the handler to define the log message format
        self.handler.setFormatter(formatter)

        # Create a logger with the specified name and set its logging level
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # Add the file handler to the logger
        self.logger.addHandler(handler)

    def assertion(self, value: bool, message: str):
        # Log an error message if the assertion fails
        if not value:
            self.logger.error(msg=message)

    def error(self, message: str):
        # Log an error message
        self.logger.error(msg=message)

    def warning(self, message: str):
        # Log a warning message
        self.logger.warning(msg=message)

    def debug(self, message: str):
        # Log a debug message
        self.logger.debug(msg=message)