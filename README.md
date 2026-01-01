<div align="center">
<h1>
    Kirosha-Team/App
</h1>
</div>

<div align="center"><img src="/docs/main_menu_interface.png" width=75% height=50%></div>

<div align="center">
<h1>
</h1>
Python application designed for gestures' controllable smart station.
</div>

## About this project

> [!IMPORTANT]
> this project is no longer being supported.

The idea for this project came after we analyzed the current smart device market. It turned out that there were no suitable devices for people with disabilities (deaf and hard of hearing people) with which to control a smart home. From that moment on, we decided to create a smart station that could solve this problem.

The [smart station from Yandex](https://alice.yandex.ru/station) became the basis of the project. We also decided to rethink the management of the station, replacing the usual voice commands with gestures. This has allowed us to increase the range of consumers, as well as simplify the use of our station.

At the moment, our smart station allows users to control their smart home using gestures and create them.

## Getting started

### Hardware requirements

> [!NOTE]
> The program requires: **1 gb** of RAM, **12 gb** of storage, **4 cores** of CPU, **any** camera, **any** display.

``Raspberry Pi 3B``
``Camera Raspberry Pi 1.3``
``TFT LCD Display 7 Inch``

##

### Software requirements

``Raspberry Pi OS (64-bit)``
``Python 3.10``

##

### Installation

> [!TIP]
> We recommend downloading the latest release to avoid bugs.

> [!WARNING]
> There might be some issues with downloading **mediapipe-model-maker**. Check out the [guide]() for installing it on **Raspberry Pi OS**.

1. Open the repository:
   ```commandline
   cd /path/to/repository
   ```
2. Create a new virtual environment:
   ```commandline
   python -m venv .venv
   ```
3. Activate the virtual environment:
   ```commandline
   source .venv/bin/activate
   ```
4. Update **pip**:
   ```commandline
   pip install --upgrade pip
   ```
5. Download packages:
   ```commandline
   pip install -r requirements.txt
   ```
6. Add weather token
   ```commandline
   dotenv set WEATHER_TOKEN 'your token here'
   ```
7. Run **setup.py**:
   ```commandline
   python setup.py
   ```
8. Run **app.py**:
   ```commandline
   python app.py
   ```

## Contribution
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
