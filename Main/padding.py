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
    
#    im = cv2.imread(directory_inv + '*.jpg')
#cv2.imshow('im', im )

#diff = 0
#diff2 = 0
#if im.shape[0] > im.shape[1] :
#    diff = im.shape[0]
#    diff2 = im.shape[1]
#else:
#    diff = im.shape[1]
#    diff2 = im.shape[0]
#    
#di = diff - diff2
#di = di/2

    pad = np.zeros((144, im.shape[1], 3), np.uint8)
#cv2.imshow('pad', pad )

    fin = np.vstack((pad, im, pad))
    cv2.imwrite(output_inv + tail, fin )
  
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
for filename_inp in glob.glob(directory_inv + '*.jpg'):
    count=count+1
#    print count
    head, tail = ntpath.split(filename_inp)
    im = cv2.imread(directory_inv + tail)
    print im.shape
#    z,Foldername=ntpath.split(head)
'''    
#img = cv2.imread(directory_inv, 1)
#print img.shape



'''
import cv2

directory_inv = 'D:/Kaggle/Invasive Species/Data/Invasive/12.jpg'
img = cv2.imread(directory_inv, 1)


img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
img_lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
b,g,r = cv2.split(img_rgb)
#cv2.imshow("img R", r)
#cv2.imshow("img G", g)
#cv2.imshow("img B", b)

#cv2.imshow("original", img)
#cv2.imshow("img_hsv", img_hsv)
cv2.imshow("img_rgb", img_rgb)
#cv2.imshow("img", img)

#cv2.imshow("img_hsv1", img_hsv[:,:,0])
#cv2.imshow("img_hsv2", img_hsv[:,:,1])
#cv2.imshow("img_hsv3", img_hsv[:,:,2])

cv2.imshow("img_lab1", img_lab[:,:,0])
cv2.imshow("img_lab2", img_lab[:,:,1])
cv2.imshow("img_lab3", img_lab[:,:,2])

cv2.imshow("img", img)

img_lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imshow("img_HSV", img_lab)
cv2.imshow("img_lab1", img_lab[:,:,0])
cv2.imshow("img_lab2", img_lab[:,:,1])
cv2.imshow("img_lab3", img_lab[:,:,2])
#gblur = cv2.GaussianBlur(img, (0, 0), 10)
#cv2.imshow('gblur', gblur )
#
#ac = cv2.addWeighted(img, 4, gblur , -4, 128)
#cv2.imshow('ac', ac )

#ba, bc, bd = cv2.split(ac)
#cv2.imshow('ba', ba )
#cv2.imshow('bc', bc )
#cv2.imshow('bd', bd )

cv2.waitKey(0)
cv2.destroyAllWindows()
'''