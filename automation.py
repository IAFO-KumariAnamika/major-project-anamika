# Import the relevant modules
import pyautogui
import time

# Give the python file some time before continuing
time.sleep(7)

# Mouse Functions
# Prints the resolution of your screen
print(pyautogui.size())
# Prints tof the mousehe current position
print(pyautogui.position())

# Moves the mouse over time (3 seconds)

pyautogui.moveTo(703, 1058, 2)
pyautogui.leftClick()

pyautogui.moveTo(519, 62, 3)
pyautogui.leftClick()

pyautogui.moveTo(38, 107, 3)
pyautogui.leftClick()

pyautogui.moveTo(677, 418, 3)
time.sleep(2)
pyautogui.leftClick()

time.sleep(3)
pyautogui.leftClick()
time.sleep(1)
pyautogui.leftClick()
time.sleep(1)
pyautogui.leftClick()
time.sleep(1)
pyautogui.leftClick()
time.sleep(1)
pyautogui.leftClick()


time.sleep(7)
pyautogui.leftClick()

time.sleep(5)
pyautogui.leftClick()

time.sleep(5)
pyautogui.leftClick()

time.sleep(5)
pyautogui.leftClick()

time.sleep(5)
pyautogui.leftClick()

time.sleep(5)
pyautogui.leftClick()

time.sleep(5)
pyautogui.leftClick()

time.sleep(5)
pyautogui.leftClick()

time.sleep(7)


# Spiral drawing using pyautogui
time.sleep(1)
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, distance, 1, button="left")
    pyautogui.dragRel(-distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, -distance, 1, button="left")
    time.sleep(2)
pyautogui.moveTo(10, 100, 3)
time.sleep(8)
#changing configuration
pyautogui.moveTo(1659, 50, 3)
pyautogui.leftClick()
pyautogui.moveTo(1661, 81, 1)
pyautogui.leftClick()
pyautogui.moveTo(1542, 274, 2)
pyautogui.leftClick()
pyautogui.moveTo(916, 560, 2)
pyautogui.leftClick()
pyautogui.moveTo(1056,780, 2)
pyautogui.leftClick()
pyautogui.moveTo(1315,898, 2)
pyautogui.leftClick()



