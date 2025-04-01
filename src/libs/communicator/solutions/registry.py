"""
    NAME: registry.py
    DESC: solution for adding, removing, rewriting devices data

    CLASS REGISTRY:
        STATIC METHODS:
            write_device --> saves device id_address, port, name, functions in file
            rewrite --> changes specific device data in file
            read_device --> returns device id_address, port, name, functions
            remove_device --> removes device file
            get_device --> returns file existence
"""

from src.utils import *
from src.constants import *

class Registry:
    @staticmethod
    def write_device(address: tuple[str, int], data: list[str]) -> None:
        port = address[1]  # Extract the port number from the address tuple

        file = DEVICES_PATH + f'/{port}.txt'  # Construct the file path using the port number

        if not Path.exists(file):  # Check if the file does not already exist
            with open(file, 'w') as file:  # Open the file in write mode
                file.write(address[0] + "\n")  # Write the device address to the file
                file.write(str(address[1]) + "\n")  # Write the port number to the file
                file.write(data[0] + "\n")  # Write the first data entry to the file

                for value in data[1:]:  # Iterate over the remaining data entries
                    file.write(value + "=none\n")  # Write each entry with a default value of 'none'

                file.close()  # Close the file (optional, as 'with' handles it)

    @staticmethod
    def rewrite_device(port: str, key: str, value: str) -> None:
        assert (type(key) is str)  # Ensure key is a string
        assert (type(port) is str)  # Ensure port is a string
        assert (type(value) is str)  # Ensure value is a string

        file = DEVICES_PATH + f'/{port}.txt'  # Construct the file path using the port number

        if Path.exists(file):  # Check if the file exists
            old_data = Registry.read_device(port)  # Read the existing data from the device file

            Registry.remove_device(port)  # Remove the old device file

            new_file = open(file, 'w')  # Open a new file in write mode

            for line in old_data:  # Iterate over each line of the old data
                if list(line.split('='))[0] == key:  # Check if the current line's key matches the provided key
                    new_file.write(key + '=' + value + "\n")  # Write the updated key-value pair
                else:
                    new_file.write(line + "\n")  # Write the unchanged line

            new_file.close()  # Close the new file

    @staticmethod
    def read_device(port: str) -> list[str]:
        assert (type(port) is str)  # Ensure port is a string

        file = DEVICES_PATH + f'/{port}.txt'  # Construct the file path using the port number

        if Path.exists(file):  # Check if the file exists
            with open(file, 'r') as file:  # Open the file in read mode
                lines = [line.split('\n')[0] for line in file.readlines()]  # Read lines and remove newline characters

            file.close()  # Close the file (optional, as 'with' handles it)

            return lines  # Return the list of lines read from the file

    @staticmethod
    def remove_device(port: str) -> None:
        assert (type(port) is str)  # Ensure port is a string

        file = DEVICES_PATH + f'/{port}.txt'  # Construct the file path using the port number

        Path.remove_file(file)  # Remove the specified file

    @staticmethod
    def get_device(address: tuple[str, int]) -> bool:
        port = address[1]  # Extract the port number from the address tuple

        file = DEVICES_PATH + f'/{port}.txt'  # Construct the file path using the port number

        return Path.exists(file)  # Return whether the file exists

    @staticmethod
    def get_devices() -> list:
        devices_data = []  # Initialize a list to hold device data

        if Path.empty(DEVICES_PATH):  # Check if the devices directory is empty
            return devices_data

        for device in os.listdir(DEVICES_PATH):  # Iterate over each file in the devices directory
            port, file_format = device.split('.')  # Split the filename to get the port number

            data = Registry.read_device(port)  # Read the device data

            devices_data.append(data)  # Append the data to the devices_data list

        return devices_data  # Return the list of device data