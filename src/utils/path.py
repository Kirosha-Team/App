import os

class Path:
    @staticmethod
    def exists(file: str):
        try:
            # Check if the file is a regular file, a symbolic link, or a directory
            return (
                    os.path.isfile(file)
                    or os.path.islink(file)
                    or os.path.isdir(file)
                    )
        except OSError:
            print(f'[ERROR]: unable to check <{file}> existence!')

    @staticmethod
    def empty(directory: str):
        return Path.size(directory) == 0

    @staticmethod
    def size(directory: str):
        try:
            # Return directory size
            return len(os.listdir(directory))
        except OSError:
            print(f'[ERROR]: unable to check <{directory}> size!')
            return 0

    @staticmethod
    def get_parent_path():
        current_path = os.getcwd()
        # Get the absolute path of the parent directory
        return Path.get_path_to(os.path.join(current_path, os.pardir))

    @staticmethod
    def get_path_to(file: str, directory=None):
        assert(type(file) is str)

        try:
            if directory:
                # Return the absolute path by joining the directory and file
                return os.path.abspath(os.path.join(directory, file))
            else:
                # Return the absolute path of the file
                return os.path.abspath(file)
        except OSError:
            print(f'[ERROR]: unable to get path to <{file}>!')

    @staticmethod
    def create_directory(directory: str):
        assert(type(directory) is str)

        try:
            # Create the directory and any necessary parent directories
            os.makedirs(directory)
        except OSError:
            print(f'[ERROR]: unable to create <{directory}> directory!')

    @staticmethod
    def remove_file(file: str, directory=None):
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
            print(f'[ERROR]: unable to remove <{file}>!')

    @staticmethod
    def clean_directory(directory: str):
        assert(type(directory) is str)

        # Get the full path of the directory to clean
        directory_path = Path.get_path_to(directory)

        # Iterate through all files in the directory and remove them
        for file in os.listdir(directory_path):
            Path.remove_file(file, directory_path)

    @staticmethod
    def remove_directory(directory: str):
        # Get the full path of the directory to be removed
        directory_path = Path.get_path_to(directory)

        try:
            if Path.exists(directory_path):
                # Clean the directory before attempting to remove it
                Path.clean_directory(directory)

                if Path.empty(directory_path):
                    # Remove the directory if it is empty
                    os.rmdir(directory_path)
                else:
                    print(f'[ERROR]: <{directory}> is not empty!')
        except OSError:
            print(f'[ERROR]: unable to remove <{directory}>!')