#-- To split collective data into Invasive and Non invasive 

import pandas as pd # dataframes
import os
import shutil

filename = 'D:/Kaggle/Invasive Species/train_labels.csv'
#aisles = pd.read_csv(filename, engine='c')
#print('Total aisles: {}'.format(aisles.shape[0]))
#aisles.head()
src_path = 'D:/Kaggle/Invasive Species/train/'
directory_inv = 'D:/Kaggle/Invasive Species/Data/Invasive'
directory_non = 'D:/Kaggle/Invasive Species/Data/Non Invasive'
#
#if not os.path.exists(directory_inv):
#    os.makedirs(directory_inv)
#    
#if not os.path.exists(directory_non):
#    os.makedirs(directory_non)

fd = pd.read_csv(filename)

for name, inv in zip(fd["name"], fd["invasive"]):
    if inv == 1:
        s_path = src_path + str(name) + '.jpg'
        shutil.move (s_path, directory_inv)
    else:
        s_path = src_path + str(name) + '.jpg'
        shutil.move (s_path, directory_non)
        