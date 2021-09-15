# Pico-BackDroid

Pico-BackDroid is a python script that install an APK payload on android with HID injection.
For CircuitPython on Raspberry Pico.

## Tested Devices

* One Plus 7 Pro - Oxygen Os 11 - Chrome
* Samsung Galaxy S7 Edge - Android 10 - Chrome

## Installation

1. Plug into you'r computer the raspberry pico. A Media drive called ```RPI-RP2``` should be mounted.

2. Download <a href="https://circuitpython.org/board/raspberry_pi_pico/">CircuitPython</a>, unzip the archive and drag and drop inside the media drive the ```.uf2``` file into it.
   That should reboot the raspberry pico, and mount it this time as ```CIRCUITPY```.

3. Download the <a href="https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/tag/20210914">adafruit-circuitpython-bundle-6.x-mpy-YYYYMMDD.zip</a> library, unzip it, and copy past the adafruit.hid directory inside CIRCUITPY lib folder.

4. Add you'r keyboard layout if needed.

5. Download <a href="https://raw.githubusercontent.com/V0lk3n/Pico-BackDroid/main/pico-backdroid.py">Pico-BackDroid script</a>, rename it code.py and save it inside the CIRCUITPY drive to overwrite the default one.

## Requirement and notes

* Actually, you should specify the device used at the beginning of the script.
* You should allow for unknown source to install the APK.
* "Google" app shouldn't be installed, otherwise depending of the configuration, the micro will appear in the google search bar in chrome and this will truncate our code.

* Depending on the Play Protect Warning, the code can be truncated. 
* Note that the code is actively under development, and i'm working into news features.

## PoC - Demo

Not released yet.
