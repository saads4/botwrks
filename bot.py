import pyautogui
import pyperclip
import time

pyautogui.click(668,1509)
pyautogui.moveTo(2,118)
pyautogui.drag(1893,1027, duration=2.0, button='left')
pyautogui.hotkey('ctrl','c')
time.sleep(3)
pyautogui.click(620,1064) #notepad
time.sleep(2)
pyautogui.click(1374,359) #curor
time.sleep(1)
pyautogui.hotkey('ctrl','v')


