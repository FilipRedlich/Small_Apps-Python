import pyautogui
import time
import webbrowser


def removeBG():
    time.sleep(3)
    for i in zdj:
        pyautogui.press(i)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.scroll(600)
    time.sleep(10)
    pyautogui.click(900, 500)


browserPath = 'C:/Program Files (x86)/Opera/launcher.exe %s'
zdj = input("Podaj nazwe zdjecia ")
webbrowser.get(browserPath).open_new_tab("https://www.remove.bg/upload")
time.sleep(10)
"""
im = pyautogui.screenshot()        # Sprawdza kolor pixela
im2 = im.getpixel((630, 230))
print(im2)
"""
check = pyautogui.pixelMatchesColor(600, 480, (74, 201, 133))
check2 = pyautogui.pixelMatchesColor(680, 230, (74, 202, 133))

if check:
    pyautogui.click(600, 480)
    removeBG()
if check2:
    pyautogui.click(630, 230)
    removeBG()
print(check)
print(check2)
