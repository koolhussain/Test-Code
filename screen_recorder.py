#This works like a screen recorder for a certain area

#numpy to convert data to numpy array as cv2 supports images as numpy array
import numpy as np
#cv2 to display the Images
import cv2
#To Grab screen 
from PIL import ImageGrab
import time

last_time = time.time()
while(True):
    #Screen captured and stored in screen varaible its not numpy array type
    #bbox=(x1,y1,x2,y2) 
    screen = ImageGrab.grab(bbox=(0,40,800,640))
    #Converting Image to numpy array using np.array and reshaping it to
    #Correct Proportions
    screen_numpy = np.array(screen.getdata(), dtype='uint8').reshape((screen.size[1],
                                                                      screen.size[0],
                                                                      3))

    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()

    #Displaying image but color is off
    #Frame rate is very slow
    cv2.imshow('Window', screen_numpy)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    
                            
    
