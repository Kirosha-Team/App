"""
    NAME: path.py
    DESC: solution for managing components' paths

    CLASS PATH:
        STATIC METHODS:
            exists --> checks the existence of component path
            empty --> checks emptiness of directory
            size --> returns amount of components inside directory
            get_path_to --> return path to component
            create_directory --> creates new directory
            remove_file --> removes file
            clean_directory --> removes all components inside directory
            remove_directory --> cleans and removes directory
"""

import os

class Path:
    @staticmethod
    def exists(file: str) -> bool:
        try:
            # Check if the file is a regular file, a symbolic link, or a directory
            return (
                    os.path.isfile(file)
                    or os.path.islink(file)
                    or os.path.isdir(file)
                    )
        except OSError:
            pass

    @staticmethod
    def empty(directory: str) -> bool:
        return Path.size(directory) == 0

    @staticmethod
    def size(directory: str) -> int:
        try:
            # Return directory size
            return len(os.listdir(directory))
        except OSError:
            return 0

    @staticmethod
    def get_path_to(file: str, directory=None) -> str:
        assert(type(file) is str)

        try:
            if directory:
                # Return the absolute path by joining the directory and file
                return os.path.abspath(os.path.join(directory, file))
            else:
                # Return the absolute path of the file
                return os.path.abspath(file)
        except OSError:
            pass

    @staticmethod
    def create_directory(directory: str) -> None:
        assert(type(directory) is str)

        try:
            # Create the directory and any necessary parent directories
            os.makedirs(directory)
        except OSError:
            pass

    @staticmethod
    def remove_file(file: str, directory=None) -> None:
        assert(type(file) is str)

        # Get the full path of the file to be removed
        file_path = Path.get_path_to(file, directory)

        try:
            if os.path.isdir(file_path):
                # If it's a directory, remove it using the remove_directory method
                Path.remove_directory(file_path)
            else:
                if Path.exists(file_path):
                    # Remove the file if it exists
                    os.unlink(file_path)
        except OSError:
            pass

    @staticmethod
    def clean_directory(directory: str) -> None:
        assert(type(directory) is str)

        # Get the full path of the directory to clean
        directory_path = Path.get_path_to(directory)

        # Iterate through all files in the directory and remove them
        for file in os.listdir(directory_path):
            Path.remove_file(file, directory_path)

    @staticmethod
    def remove_directory(directory: str) -> None:
        # Get the full path of the directory to be removed
        directory_path = Path.get_path_to(directory)

        try:
            if Path.exists(directory_path):
                # Clean the directory before attempting to remove it
                Path.clean_directory(directory)

                if Path.empty(directory_path):
                    # Remove the directory if it is empty
                    os.rmdir(directory_path)
        except OSError:
            pass