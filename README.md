# Pico-BackDroid

Pico-BackDroid is a python script that install an APK payload on an android device with HID injection. For CircuitPython on Raspberry Pi Pico.

I created this project for fun, and up my knowledges. After getting fun with Pico-Ducky, I decided to make a project myself against Android.

Use it ethicaly!

## Tested Devices

### One Plus
* One Plus 7 Pro - Oxygen Os 11
* One Plus 8 Pro - Oxygen Os 11 - Unstable

### Samsung
* Samsung Galaxy S7 Edge - Android 10

### Note
* Test it on your device, and make pull request!

## Tested Keyboard Layout
* Swiss France - QWERTZ

## Installation

1. Plug into you'r computer the Raspberry Pi Pico. A Media drive called ```RPI-RP2``` should appear.

2. Download <a href="https://circuitpython.org/board/raspberry_pi_pico/">CircuitPython</a>, drag and drop inside the media drive the downloaded ```.uf2``` file into it.
   That should reboot the raspberry pico, and mount it this time as ```CIRCUITPY```.

3. Download the <a href="https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/tag/20210914">adafruit-circuitpython-bundle-6.x-mpy-YYYYMMDD.zip</a> library, unzip it, and copy past the ```adafruit.hid``` directory inside ```CIRCUITPY``` ```lib``` folder.

4. Add you'r keyboard layout if needed (Actually setup on Swiss French "QWERTZ" Keyboard Layout). Reffer to <a href="https://github.com/dbisu/pico-ducky/issues/10">this issue</a> of Pico-Ducky GitHub Repository.

5. Download <a href="https://raw.githubusercontent.com/V0lk3n/Pico-BackDroid/main/pico-backdroid.py">Pico-BackDroid script</a>, rename it ```code.py``` and save it inside the ```CIRCUITPY``` drive to overwrite the default one.

## Requirement and notes

1. You should specify the device used at the beginning of the script. (Working on a PIN version where it pick the device depending which pin is connected)
2. Generate your payload, change the URL into the script to your apk file.
3. You should allow for unknown source before runing it against the target device.
4. Chrome should be the default browser used everywhere to avoid to chose which browser open.

## Fix and Todo

* Fix keyboard layout which is alway QWERTY in android device.
* Try to add OnePlus8 Device on the Pin version.
* Try the Pin version using selector.
* Create a Wiki.

<b>Note that the code is actively under development, and i'm working into news features.</a>

## PoC - Demo

Not released yet.
