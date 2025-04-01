from io import BytesIO
from urllib import request
from zipfile import ZipFile

from src.utils import *
from src.constants import *

def download_model() -> None:
    # Download the model from the specified link and save it to the asset path
    request.urlretrieve(MODEL_LINK, ASSET_PATH)

def download_samples() -> None:
    gesture_recognizer_path = GESTURE_RECOGNIZER_PATH

    # Open the URL containing the samples and read the data
    samples = request.urlopen(SAMPLES_LINK)
    # Create a ZipFile object from the downloaded samples
    archive = ZipFile(BytesIO(samples.read()))

    # Extract all contents of the zip file to the specified path
    archive.extractall(gesture_recognizer_path)

    # Rename the extracted folder to the datasets path
    os.rename(os.path.join(gesture_recognizer_path, 'rps_data_sample'), DATASETS_PATH)

if __name__ == '__main__':
    # Create the devices directory if it doesn't exist
    Path.create_directory(DEVICES_PATH)
    # Create the model directory if it doesn't exist
    Path.create_directory(MODEL_PATH)
    # Create the logs directory if it doesn't exist
    Path.create_directory(LOGS_PATH)

    download_model()
    download_samples()