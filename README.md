# Image-Manipulation-with-Python-Pixel-Color-Replacement

2. Features
Image Loading: Loads an image from a file.
Pixel Manipulation: Iterates through each pixel in the image and modifies the color values based on specified conditions.
Image Display: Displays the modified image.
3. System Requirements
Python 3.6 or later
PIL (Pillow) library
NumPy library
A terminal or command-line interface
Jupyter Notebook or an IPython environment (optional for inline display)
4. Installation
Install Required Libraries:
Ensure you have Pillow and NumPy installed. You can install them using pip:

bash
Copy code
pip install pillow numpy
Clone the Repository: Clone this repository to your local machine using:

bash
Copy code
git clone <repository_url>
Navigate to the Directory:

bash
Copy code
cd <repository_directory>
Run the Script:

bash
Copy code
python image_manipulation.py
Replace <repository_url> and <repository_directory> with the actual URL and directory name.

5. Usage
Place an Image: Ensure you have an image named test.jpg in the same directory as your script.

Run the Script: Execute the script to load, modify, and display the image.

6. Code Overview
Import Libraries
python
Copy code
from PIL import Image
import numpy as np
from IPython.display import display
Load the Image
python
Copy code
img = Image.open('test.jpg')
Opens the image test.jpg using PIL.
Convert Image to NumPy Array
python
Copy code
img_array = np.array(img)
Converts the image into a NumPy array for pixel manipulation.
Get Image Dimensions
python
Copy code
height, width = img_array.shape[:2]
Retrieves the height and width of the image.
Modify Pixel Colors
python
Copy code
for i in range(width):
    for j in range(height):
        if img_array[j, i, 0] < 120 and img_array[j, i, 1] < 120 and img_array[j, i, 2] < 120:
            img_array[j, i] = [255, 255, 255]  # White
        else:
            img_array[j, i] = [255, 255, 0]  # Yellow
Changes pixels with RGB values below 120 to white, and all others to yellow.
Convert Back to Image and Display
python
Copy code
modified_img = Image.fromarray(img_array)
modified_img.show()
Converts the modified NumPy array back into an image and displays it.
