"""
NAME: zone.py
DESC: solution for tracking time, date, datetime and weather

CLASS CLOCK:
    STATIC METHODS:
        get_time --> returns current time in hours and minutes
        get_date --> returns current date
        get_weekday --> returns current weekday

CLASS WEATHER:
    STATIC METHODS:
        get_temperature --> returns the current temperature depending on the location
"""

import time, datetime

from os import (
    environ,
)
from dotenv import *

from src.libs.communicator.solutions.communicator import (
    CommunicatorUtils,
)
from src.constants import *

load_dotenv()


class Clock:
    @staticmethod
    def get_time():
        return time.strftime(TIME_FORMAT)

    @staticmethod
    def get_date():
        return datetime.date.today()

    @staticmethod
    def get_weekday(
        date: any,
    ):
        return WEEKDAYS[datetime.date.weekday(date)]


class Weather:
    @staticmethod
    def get_temperature():
        location = CommunicatorUtils.request(LOCATION_LINK)

        if not location:
            return NO_TEMPERATURE

        link = WEATHER_LINK.format(
            location["city"],
            environ.get("WEATHER_TOKEN"),
        )

        weather_info = CommunicatorUtils.request(link)

        if weather_info["cod"] == 401:
            return NO_TEMPERATURE

        temperature = weather_info["main"]["temp"]

        return round(temperature)
