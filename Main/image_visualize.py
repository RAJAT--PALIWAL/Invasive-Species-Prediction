
import cv2
import glob
import ntpath
import numpy as np

directory_inv = 'D:/Kaggle/Invasive Species/Data/mauka/'
output_inv = 'D:/Kaggle/Invasive Species/Data/mauka2/'

for filename_inp in glob.glob(directory_inv + '*.jpg'):
    
    head, tail = ntpath.split(filename_inp)
    im = cv2.imread(directory_inv + tail)
    
    flipped = cv2.flip(im, 1)
    
    cv2.imshow(output_inv + tail, im)
    cv2.imshow(output_inv + 'flipped_' + tail, flipped )
  
cv2.waitKey(0)
cv2.destroyAllWindows()
    
