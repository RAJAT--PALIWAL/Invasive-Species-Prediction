'''
Script to feed image as it is to the CNN
Padding the rectangular image to make it square

'''
#Analyze the shape of all the images
import cv2
import glob
import ntpath
import numpy as np

directory_inv = 'D:/Kaggle/Invasive Species/Data/Non Invasive/'
output_inv = 'D:/Kaggle/Invasive Species/Data/Padded images/Non_Invasive/'

for filename_inp in glob.glob(directory_inv + '*.jpg'):
    
    head, tail = ntpath.split(filename_inp)
    im = cv2.imread(directory_inv + tail)
    

    pad = np.zeros((144, im.shape[1], 3), np.uint8)

    fin = np.vstack((pad, im, pad))
    cv2.imwrite(output_inv + tail, fin )
  
cv2.waitKey(0)
cv2.destroyAllWindows()
