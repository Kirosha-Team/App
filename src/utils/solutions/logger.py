"""
NAME: logger.py
DESC: solution for catching errors, warnings, debugs

CLASS LOGGER UTILS:
    STATIC METHODS:
        convert --> returns text with replaced $ with /n

CLASS LOGGER:
    PRIVATE METHODS:
        __init__ --> initializes solution

    PUBLIC METHODS:
        error --> logs error in .log file
        warning --> logs warning in .log file
        debug --> logs debug in .log file
"""

import logging

from src.utils.solutions.path import *

from src.constants import *


class LoggerUtils:
    @staticmethod
    def convert(
        message: str,
    ) -> str:
        return f"${message}".replace(
            OLD_SIGNATURE,
            NEW_SIGNATURE,
        )


class Logger:
    def __init__(
        self,
        name: str,
    ):
        assert type(name) is str

        self.handler = handler = logging.FileHandler(
            filename=Path.get_path_to(
                f"{name}.log",
                LOGS_PATH,
            ),
            mode="w",
        )

        self.formatter = logging.Formatter(LOGGING_FORMAT)

        self.handler.setFormatter(self.formatter)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(handler)

    def error(
        self,
        message: str,
    ) -> None:
        self.logger.error(msg=LoggerUtils.convert(message + "$if this error occur -> run setup.py$then restart main.py"))

    def warning(
        self,
        message: str,
    ) -> None:
        self.logger.warning(msg=LoggerUtils.convert(message + "$this warning can be ignored"))

    def debug(
        self,
        message: str,
    ) -> None:
        self.logger.debug(msg=LoggerUtils.convert(message))
