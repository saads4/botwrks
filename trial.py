import pyautogui
import time
def screen_capture(image_name):
   time.sleep(1)
   screenshot = pyautogui.screenshot(region=(333,118,753,347))
   screenshot.save(image_name)
screen_capture(image_name="screen1.png")
time.sleep(30)
screen_capture(image_name="screen2.png")
