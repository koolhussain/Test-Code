#This works like a screen recorder for a certain area

#numpy to convert data to numpy array as cv2 supports images as numpy array
import numpy as np
#cv2 to display the Images
import cv2
#To Grab screen 
from PIL import ImageGrab
#import time have an idea about frames per second
import time

def process_img(image):
    processed_img = cv2.Canny(image, threshold1 = 200, threshold2 = 300)
    return processed_img

last_time = time.time()
while(True):
    #Screen captured and stored in screen varaible its not numpy array type
    #bbox=(x1,y1,x2,y2) 
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,600)).convert('L'))
    screen = process_img(screen)
    
    #printing time taken in each loop or time taken to process each frame 
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    
    #Displaying image but color is off
    #Frame rate is very slow
    cv2.imshow('Window', screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    
                            
    
