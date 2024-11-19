import pyautogui
import time
from PIL import Image
import numpy as np
import os
#funtion to deletethefile after comparision
def delete(file_path):
  os.remove(file_path)
#function to take a screenshot and save it
def screen_capture(image_name):
   screenshot = pyautogui.screenshot(region=(333,118,753,347))
   screenshot.save(image_name)
duration = 10
# Record the start time
start_time = time.time()
while True:
  if time.time() - start_time > duration:
    break
  
  image1=screen_capture(image_name="screen1.png") #function call out 1
  time.sleep(0.1) #to add time to for second screen shot
  image2=screen_capture(image_name="screen2.png") #function call out 2
  image1 = Image.open("screen1.png") #to open two image for comaprision
  image2 = Image.open("screen2.png") #to open two image for comaprision

  array1 = np.array(image1) #to convert image to pixels
  array2 = np.array(image2) #to convert image to pixels


  if np.array_equal(array1, array2): #comparision of two pixels
     print("Images are identical.")
     pyautogui.hotkey('N','O','T','Space','J','U','M','P')
  else:
     print("Images are different.")
     pyautogui.hotkey('space','J','U','M','P')

  delete(file_path=r"C:\Users\SAAD\Documents\Coding\screen1.png")
  delete(file_path=r"C:\Users\SAAD\Documents\Coding\screen2.png")