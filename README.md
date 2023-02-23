# honk_screen

It takes 5 pictures of Honka and lets them fall and rotate randomly

# Requies

* python >=3.9.6
* pygame

`python -m pip install pygame`

# To run

1. Clone this repo

`git clone https://github.com/SozinovD/honk_screen`

2. go to repo dir

`cd honk_screen`

3. Run main screen

`python Honka_fullscreen.py`

4. Press "ESC" to exit

# To make an executable file (Windows)

1. Install pyinstaller

`python -m pip install pyinstaller`

2. Run this command in project dir

`pyinstaller.exe '.\Honka_fullscreen.py' --onefile --noconsole --add-data='*.png;.'`
