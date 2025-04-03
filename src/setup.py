from io import BytesIO
from urllib import request
from zipfile import ZipFile

from src.utils import *
from src.constants import *

def download_model() -> None:
    request.urlretrieve(MODEL_LINK, ASSET_PATH)

def download_samples() -> None:
    gesture_recognizer_path = GESTURE_RECOGNIZER_PATH

    samples = request.urlopen(SAMPLES_LINK)

    archive = ZipFile(BytesIO(samples.read()))
    archive.extractall(gesture_recognizer_path)

    os.rename(os.path.join(gesture_recognizer_path, 'rps_data_sample'), DATASETS_PATH)

if __name__ == '__main__':
    Path.create_directory(DEVICES_PATH)
    Path.create_directory(MODEL_PATH)
    Path.create_directory(LOGS_PATH)

    download_model()
    download_samples()