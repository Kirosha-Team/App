"""
    NAME: communicator.py
    DESC: solution for sending and receiving data using Wi-Fi

    CLASS COMMUNICATOR UTILS:
        STATIC METHODS:
            get_ip_address --> returns ip address
            decode --> converts received data into tuple
            encode --> converts data to send into bytes

    CLASS COMMUNICATOR:
        PRIVATE METHODS:
            __init__ --> initializes util

        PUBLIC METHODS:
            start --> starts listening and callbacks data, address
            stop --> stops listening
            send --> sends data to address
"""

import socket

from src.constants import *

class CommunicatorUtils:
    @staticmethod
    def get_ip_address() -> str:
        # Create a UDP socket
        temporary_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            # Connect to a public DNS server (Google's 8.8.8.8) on port 80
            temporary_socket.connect(("8.8.8.8", 80))

            # Return the local IP address of the socket
            return temporary_socket.getsockname()[0]
        finally:
            # Ensure the socket is closed after use
            temporary_socket.close()

    @staticmethod
    def decode(data: bytes) -> list[str]:
        # Decode the byte data to a string using UTF-8 and split it by underscores
        return data.decode('utf-8').split('_')

    @staticmethod
    def encode(data: str) -> bytes:
        # Ensure the input data is of type string
        assert (type(data) is str)

        length = len(data)

        # If the string is shorter than 10 characters, pad it with hyphens
        if length < 10:
            data += '-' * (10 - length)

        # Convert the string to bytes using UTF-8 encoding
        return bytes(data, 'utf-8')

class Communicator:
    def __init__(self, listener: callable):
        assert(callable(listener))  # Ensure the listener is a callable function

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket

        # self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # Uncomment to allow multiple sockets to bind to the same port
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting on the socket

        self.socket.bind(('', LOCAL_PORT))  # Bind the socket to the local port

        self._running = False  # Initialize the running state to False
        self._callback = listener  # Store the listener callback function

    def start(self) -> None:
        assert(self._running is False)  # Ensure the communicator is not already running

        self._running = True  # Set the running state to True

        while self._running:  # Continue running while the communicator is active
            data, address = self.socket.recvfrom(BUFFER_SIZE)  # Receive data from the socket

            if data is not None:  # Check if data is received
                data = CommunicatorUtils.decode(data)  # Decode the received data

                self._callback(data, address)  # Call the listener with the decoded data and address

    def stop(self) -> None:
        assert(self._running is True)  # Ensure the communicator is currently running

        self._running = False  # Set the running state to False

    def send(self, address: tuple[str, int], command: str) -> None:
        command = CommunicatorUtils.encode(command)  # Encode the command to bytes

        self.socket.sendto(command, address)  # Send the encoded command to the specified address

    def is_running(self) -> bool:
        return self._running  # Return the current running state