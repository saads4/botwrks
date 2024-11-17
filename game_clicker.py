import pyautogui
import time
from PIL import Image
import numpy as np
def screen_capture(image_name):
   time.sleep(10)
   screenshot = pyautogui.screenshot(region=(333,118,753,347))
   screenshot.save(image_name)
image1=screen_capture(image_name="screen1.png")
time.sleep(5)
image2=screen_capture(image_name="screen2.png")
image1 = Image.open("screen1.png")
image2 = Image.open("screen2.png")


array1 = np.array(image1)
array2 = np.array(image2)


if np.array_equal(array1, array2):
    print("Images are identical.")
else:
    print("Images are different.")
    pyautogui.hotkey('space')


