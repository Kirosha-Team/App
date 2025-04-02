<div align="center">
<h1>
    KiroshaTeam/App
</h1>
Python application designed for Raspberry Pi devices
</div>

<hr style="border:2px solid gray">

<div>
<h2>
    <img src="https://media.discordapp.net/attachments/773798084479418389/1356951990814511324/info.png?ex=67ee6f85&is=67ed1e05&hm=e1740f9b9cb79ba5ec35c9fc308815ab9eb437bb2eaa59931e9a4cbdd285022e&=&format=webp&quality=lossless" alt="Info" style="width:5%">
    About this project:
</h2>
The <a href="https://alice.yandex.ru/station">smart station from Yandex</a> became the basis of the project. We also decided to rethink the management of the station, replacing the usual voice commands with gestures. This has allowed us to increase the range of consumers, as well as simplify the use of our station.
</div>

<hr style="border:2px solid gray">

<div>
<h2>
    <img src="https://media.discordapp.net/attachments/773798084479418389/1356951991594778849/scanner-image.png?ex=67ee6f85&is=67ed1e05&hm=8992ceb409d51eea065d93e1fdbd80b174a3cf571590c9cd52b606076cf72bb0&=&format=webp&quality=lossless" alt="Hardware" style="width:5%">
    Hardware requirements:
</h2>

<img src="https://assets.raspberrypi.com/static/532b4c25752c4235d76cc41051baf9ab/9ff6b/877fb653-7b43-4931-9cee-977a22571f65_3b%2BAngle%2B2%2Brefresh.webp" alt="Board" style="width:30%"><img src="https://assets.raspberrypi.com/static/6a75fa481019db1ac6bca74e5192cb5b/9ff6b/ffa68a46-fd44-4995-9ad4-ac846a5563f1_Camera%2BV2%2BHero.webp" alt="Camera" style="width:30%"><img src="https://assets.raspberrypi.com/static/d93d3a26f4525829f55b34372cf65a5e/9ff6b/ZySo0K8jQArT0HDZ_TouchDisplay2desktop.webp" alt="Display" style="width:30%">

</div>

<hr style="border:2px solid gray">

<div>
<h2>
    <img src="https://media.discordapp.net/attachments/773798084479418389/1356952020011188224/software-development1.png?ex=67ee6f8c&is=67ed1e0c&hm=05533707ce75a34dd803b3909eb4eeb7299d01074b0366e988562442e264e7e2&=&format=webp&quality=lossless" alt="Software" style="width:5%">
    Software requirements:
</h2>
</div>

``Raspberry Pi OS (64-bit)``
``Python 3.10``

<hr style="border:2px solid gray">

<div>
<h2>
    <img src="https://media.discordapp.net/attachments/773798084479418389/1356951991246520480/down.png?ex=67ee6f85&is=67ed1e05&hm=dcf9e13db4156f3b5a8f062633fdc4beca58bf37ab85636d8566d31faaf5f2b2&=&format=webp&quality=lossless" alt="Download" style="width:5%">
    Installation:
</h2>
New repository releases can be found <a href="https://github.com/Kirosha-Team/App/releases">here</a>
</div>

`1` Open the repository:

    cd /path/to/repository
`2` Create a new virtual environment:

    python -m venv .venv
`3` Activate the virtual environment:
    
    source .venv/bin/activate
`4` Update **pip**:

    pip install --upgrade pip
`5` Download packages:
    
    pip install -r requirements.txt
`6` Run **setup.py**:
    
    python setup.py
`7` Add **app.py** to startup and then restart:
    
    sudo nano /etc/profile
    python main.py &
    sudo reboot

<hr style="border:2px solid gray">

<div>
<h2>
    <img src="https://media.discordapp.net/attachments/773798084479418389/1356950282562441348/heart-Photoroom.png?ex=67ee6dee&is=67ed1c6e&hm=d4ecb6c4cfb100f682d95f263c7f4bbb87967c55140c92f1e12e837b57937872&=&format=webp&quality=lossless" alt="Heart" style="width:5%">
    Contribution:
</h2>
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
</div>