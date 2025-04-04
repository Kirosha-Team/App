"""
    NAME: communicator.py
    DESC: solution for sending and receiving data using Wi-Fi

    CLASS COMMUNICATOR UTILS:
        STATIC METHODS:
            get_ip_address --> returns ip address
            request --> returns response data
            decode --> converts received data into tuple
            encode --> converts data to send into bytes

    CLASS COMMUNICATOR:
        PRIVATE METHODS:
            __init__ --> initializes solution

        PUBLIC METHODS:
            start --> starts listening and callbacks data, address
            stop --> stops listening
            send --> sends data to address
"""

import socket, requests

from requests import *

from src.constants import *

class CommunicatorUtils:
    @staticmethod
    def get_ip_address() -> str:
        temporary_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            temporary_socket.connect(("8.8.8.8", 80))

            return temporary_socket.getsockname()[0]
        finally:
            temporary_socket.close()

    @staticmethod
    def request(url: str):
        try:
            response = requests.get(url)

            return response.json()
        except HTTPError:
            pass

    @staticmethod
    def decode(data: bytes) -> list[str]:
        return data.decode('utf-8').split('_')

    @staticmethod
    def encode(data: str) -> bytes:
        assert (type(data) is str)

        length = len(data)

        if length < 10:
            data += '-' * (10 - length)

        return bytes(data, 'utf-8')

class Communicator:
    def __init__(self, listener: callable):
        assert(callable(listener))

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.socket.bind(('', LOCAL_PORT))

        self._running = False
        self._callback = listener

    def start(self) -> None:
        assert(self._running is False)

        self._running = True

        while self._running:
            data, address = self.socket.recvfrom(BUFFER_SIZE)

            if data is not None:
                data = CommunicatorUtils.decode(data)

                self._callback(data, address)

    def stop(self) -> None:
        assert(self._running is True)

        self._running = False

    def send(self, address: tuple[str, int], command: str) -> None:
        command = CommunicatorUtils.encode(command)

        self.socket.sendto(command, address)

    def is_running(self) -> bool:
        return self._running