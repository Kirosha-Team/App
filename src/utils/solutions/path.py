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
    def exists(
        file: str,
    ) -> bool:
        try:
            return os.path.isfile(file) or os.path.islink(file) or os.path.isdir(file)
        except OSError:
            pass

    @staticmethod
    def empty(
        directory: str,
    ) -> bool:
        return Path.size(directory) == 0

    @staticmethod
    def size(
        directory: str,
    ) -> int:
        try:
            return len(os.listdir(directory))
        except OSError:
            return 0

    @staticmethod
    def get_path_to(
        file: str,
        directory=None,
    ) -> str:
        assert type(file) is str

        try:
            if directory:
                return os.path.abspath(
                    os.path.join(
                        directory,
                        file,
                    )
                )
            else:
                return os.path.abspath(file)
        except OSError:
            pass

    @staticmethod
    def create_directory(
        directory: str,
    ) -> None:
        assert type(directory) is str

        try:
            os.makedirs(directory)
        except OSError:
            pass

    @staticmethod
    def remove_file(
        file: str,
        directory=None,
    ) -> None:
        assert type(file) is str

        file_path = Path.get_path_to(
            file,
            directory,
        )

        try:
            if os.path.isdir(file_path):
                Path.remove_directory(file_path)
            else:
                if Path.exists(file_path):
                    os.unlink(file_path)
        except OSError:
            pass

    @staticmethod
    def clean_directory(
        directory: str,
    ) -> None:
        assert type(directory) is str

        directory_path = Path.get_path_to(directory)

        for file in os.listdir(directory_path):
            Path.remove_file(
                file,
                directory_path,
            )

    @staticmethod
    def remove_directory(
        directory: str,
    ) -> None:
        directory_path = Path.get_path_to(directory)

        try:
            if Path.exists(directory_path):
                Path.clean_directory(directory)

                if Path.empty(directory_path):
                    os.rmdir(directory_path)
        except OSError:
            pass
