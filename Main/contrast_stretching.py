import numpy as np
import cv2
import matplotlib.pylab as plt
from scipy.misc import imread
import glob
import os

'''
def scaleRadius(img,scale):
        x=img[img.shape[0]/2,:,:].sum(1)
        r=(x>x.mean()/10).sum()/2
        s=scale*1.0/r
        return cv2.resize(img,(0,0),fx=s,fy=s)

scale = 350
        
def stretch_n(bands, lower_percent=1, higher_percent=99):
    out = np.zeros_like(bands).astype(np.float32)
    n = bands.shape[2]
    for i in range(n):
        a = 0  # np.min(band)
        b = 1  # np.max(band)
        c = np.percentile(bands[:, :, i], lower_percent)
        d = np.percentile(bands[:, :, i], higher_percent)
        t = a + (bands[:, :, i] - c) * (b - a) / (d - c)
        t[t < a] = a
        t[t > b] = b
        out[:, :, i] = t
    return out.astype(np.float32)

file_path = 'D:/Kaggle/Invasive Species/Data/Invasive/61.jpg'
#file_path = 'C:/Users/524316/Desktop/Negative Kaggle images/10166_right.jpeg'
img = cv2.imread(file_path)
#img = scaleRadius(img, scale)

img1 = stretch_n(img)

cv2.imshow('orig', img)
cv2.imshow('contrast_stretch', img1)

cv2.waitKey()
cv2.destroyAllWindows()
'''

def stretch_n(bands, lower_percent=1, higher_percent=99):
    out = np.zeros_like(bands).astype(np.float32)
    n = bands.shape[2]
    for i in range(n):
        a = 0  # np.min(band)
        b = 1  # np.max(band)
        c = np.percentile(bands[:, :, i], lower_percent)
        d = np.percentile(bands[:, :, i], higher_percent)
        t = a + (bands[:, :, i] - c) * (b - a) / (d - c)
        t[t < a] = a
        t[t > b] = b
        out[:, :, i] = t
    return out.astype(np.float32)
    
output_path = 'D:/Kaggle/Invasive Species/Data/mauka2/'
file_loc = 'D:/Kaggle/Invasive Species/Data/mauka/'
for filename_inp in glob.glob(file_loc + '*.jpg'):
    
    print filename_inp
    inp = os.path.basename(filename_inp).split('_')[0]
    print inp
    
    img = cv2.imread(filename_inp)
    img1 = stretch_n(img, lower_percent=1, higher_percent=99)
#    cv2.imshow(output_path + inp + '.jpg', img1)
#    cv2.imshow('orig', img)
    
    
    img2 = img1 * 255
    img2 = img2.astype(np.uint16)
    cv2.imwrite(output_path + inp +'.jpg', img2)
    
    cv2.waitKey()
cv2.destroyAllWindows() 