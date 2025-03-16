import socket

def get():
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