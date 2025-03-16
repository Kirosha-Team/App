"""
    NAME: communicator.py

    DESC: solution for sending and receiving data using Wi-Fi

    PRIVATE METHODS:
        __init__ -> initializes util

    PUBLIC METHODS:
        start -> starts listening and callbacks data, address
        stop -> stops listening
        send -> sends data to address
"""

import socket

from src.utils import byte
from src.constants import LOCAL_PORT
from src.constants import BUFFER_SIZE

class Communicator:
    def __init__(self, listener):
        assert(callable(listener))  # Ensure the listener is a callable function

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket

        # self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # Uncomment to allow multiple sockets to bind to the same port
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting on the socket

        self.socket.bind(('', LOCAL_PORT))  # Bind the socket to the local port

        self._running = False  # Initialize the running state to False
        self._callback = listener  # Store the listener callback function

    def start(self):
        assert(self._running is False)  # Ensure the communicator is not already running

        self._running = True  # Set the running state to True

        while self._running:  # Continue running while the communicator is active
            data, address = self.socket.recvfrom(BUFFER_SIZE)  # Receive data from the socket

            if data is not None:  # Check if data is received
                data = byte.decode(data)  # Decode the received data

                self._callback(data, address)  # Call the listener with the decoded data and address

    def stop(self):
        assert(self._running is True)  # Ensure the communicator is currently running

        self._running = False  # Set the running state to False

    def send(self, address: tuple[str, int], command: str):
        command = byte.encode(command)  # Encode the command to bytes

        self.socket.sendto(command, address)  # Send the encoded command to the specified address

    def is_running(self):
        return self._running  # Return the current running state