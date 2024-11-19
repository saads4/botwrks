from PIL import Image
import numpy as np
import os


# Load the images
image1 = Image.open("screen1.png")
image2 = Image.open("screen2.png")

# Convert images to numpy arrays
array1 = np.array(image1)
array2 = np.array(image2)

# Check if they are identical
if np.array_equal(array1, array2):
    print("Images are identical.")
else:

    print("Images are different.")

import os

# Specify the file path
file_path = r"C:\Users\SAAD\Pictures\Camera Roll\Saad Pic .jpg"

# Attempt to delete the file
os.remove(file_path)
print(f"{file_path} has been deleted.")






