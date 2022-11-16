<h1>sound_of_mouse</h1>

<h2>Table of content</h2>

- [Description](#description)
- [Install](#install)
- [Usage](#usage)
- [To Do](#to-do)

## Description ##
**Задание:**
написать на python программу в ООП стиле, которая генерирует звуки(любые) в зависимости от скорости и направления движения мышкой. (двигаешь мышь, получаешь звук).

## Install ##
**To install run one of these block POSIX terminal**

- if You use poetry:
```
git clone https://github.com/sunCelery/sound_of_mouse.git && \
cd sound_of_mouse && \
poetry install
```
- else:
```
git clone https://github.com/sunCelery/sound_of_mouse.git && \
cd sound_of_mouse && \
python -m venv .venv && source .venv/bin/activate && \
python -m pip install --upgrade pip && pip install -r requirements.txt
```

## Usage ##
**To launch app run one of these block POSIX terminal**

- if You use poetry:
```
poetrry run python sound_of_mouse.py
```
- else:
```
python sound_of_mouse.py
```

Here You could hear the beutiful sound any-time You are moving a mouse.

## To Do ##
1. refactor program code to OOP style
2. fix app crash bug
3. make code clean and PEP8 friendly
4. reduce CPU usage of the app
