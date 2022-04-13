import pyautogui
width, height = pyautogui.size()
#print(pyautogui.position())
#pyautogui.moveTo(665,115)
"""
pyautogui.click(665,115)
try:
    while True:
        pyautogui.press('W',presses=3,interval=0.5)
        pyautogui.press('D',presses=3,interval=0.5)
        pyautogui.press('S',presses=3,interval=0.5)
        pyautogui.press('A',presses=3,interval=0.5)
except KeyboardInterrupt:
    print("\nDone")
"""
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print("\nDone")