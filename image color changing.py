from PIL import Image
import numpy as np
from IPython.display import display


# Load the image
img = Image.open('test.jpg')  

# Convert the image to a NumPy array
img_array = np.array(img)

# Get the height and width of the image
height = img_array.shape[0]
width = img_array.shape[1]

img_array = np.array(img)
img_array.shape

""" The RGB Values of the first Pixel """
img_array[0][0]

""" You can use the height and width variables in your code to get the rows and columns of pixels in the image """
height = img_array.shape[0]
width = img_array.shape[1]
height,width


for i in range(width):
    for j in range(height):
        if (img_array[j, i, 0] < 120 and img_array[j, i, 1] < 120 and img_array[j, i, 2] < 120):
            img_array[j, i, 0] = 255
            img_array[j, i, 1] = 255
            img_array[j, i, 2] = 255
        else:
            img_array[j, i, 0] = 255
            img_array[j, i, 1] = 255
            img_array[j, i, 2] = 0

modified_img = Image.fromarray(img_array)

print (modified_img)
modified_img.show()    