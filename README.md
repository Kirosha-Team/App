<div align="center">
<h1>
    KiroshaTeam/App
</h1>
Python application designed for gestures' controllable smart station.
</div>

## About this project
The [smart station from Yandex]("https://alice.yandex.ru/station") became the basis of the project. We also decided to rethink the management of the station, replacing the usual voice commands with gestures. This has allowed us to increase the range of consumers, as well as simplify the use of our station.

## Hardware requirements
<img src="https://assets.raspberrypi.com/static/532b4c25752c4235d76cc41051baf9ab/9ff6b/877fb653-7b43-4931-9cee-977a22571f65_3b%2BAngle%2B2%2Brefresh.webp" alt="Board" style="width:30%"><img src="https://assets.raspberrypi.com/static/6a75fa481019db1ac6bca74e5192cb5b/9ff6b/ffa68a46-fd44-4995-9ad4-ac846a5563f1_Camera%2BV2%2BHero.webp" alt="Camera" style="width:30%"><img src="https://assets.raspberrypi.com/static/d93d3a26f4525829f55b34372cf65a5e/9ff6b/ZySo0K8jQArT0HDZ_TouchDisplay2desktop.webp" alt="Display" style="width:30%">

> [!NOTE]
> The program requires: **1 gb** of RAM, **10 gb** of storage, **4 cores** of CPU 

## Software requirements
``Raspberry Pi OS (64-bit)``
``Python 3.10``

## Installation
> [!TIP]
> We recommend downloading the latest release to avoid bugs.

> [!WARNING]
> There might be some issues with downloading **mediapipe-model-maker**. Check out the [guide]() for installing it on raspberry os

1. Open the repository:

    ```
    cd /path/to/repository
   ```
2. Create a new virtual environment:

    ```
    python -m venv .venv
   ```
3. Activate the virtual environment:
    
    ```
    source .venv/bin/activate
   ```
4. Update **pip**:

    ```
    pip install --upgrade pip
   ```
5. Download packages:
    
    ```
    pip install -r requirements.txt
   ```
6. Run **setup.py**:
    
    ```
    python setup.py
   ```
7. Add **app.py** to startup and then restart:
    
    ```
   sudo nano /etc/profile
   python main.py &
   sudo reboot
   ```

## Contribution
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.