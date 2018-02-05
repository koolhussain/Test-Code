#This works like a screen shot of the whole screen




#numpy to convert data to numpy array as cv2 supports images as numpy array
import numpy as np
#cv2 to display the Images
import cv2
#To Grab screen 
from PIL import ImageGrab


#Screen captured and stored in screen varaible its not numpy array type
screen = ImageGrab.grab()
#Converting Image to numpy array using np.array and reshaping it to
#Correct Proportions
screen_numpy = np.array(screen.getdata(), dtype='uint8').reshape((screen.size[1],
                                                                  screen.size[0],
                                                                  3))

#Displaying image but color is off
cv2.imshow('Window', screen_numpy)
if cv2.waitKey(25) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    
