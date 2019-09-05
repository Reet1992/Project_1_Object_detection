import numpy as np
from PIL import ImageGrab
import cv2
import time
#import pyautogui
from numpy import ones,vstack
from numpy.linalg import lstsq
#from directkeys import PressKey,ReleaseKey, W, A, S, D
from statistics import mean
import ctypes
import time
import os
import win32api as wapi

keybox=["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keybox.append(char)

def key_check():
    keys=[]
    for key in keybox:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)

    return keys




def keys_to_output(keys):

    #[A,W,D]
    result=[0,0,0]

    if 'A' in keys:
        result[0]=1
    elif 'D' in keys:
        result[2]=1
    else:
        result[1]=1

    return result
    
file_name='training_data_13.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_value=list(np.load(file_name))
else:
    print('File does not exist,starting fresh')
    training_value=[]
    
    

def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)


last_time = time.time()
while True:
    screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    screen =  cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    screen =  cv2.resize(screen,(100,80))
    keys=key_check()
    result=keys_to_output(keys)
    training_value.append([screen,result])
    print('Frame took {} seconds'.format(time.time()-last_time))
    last_time = time.time()

    if len(training_value) % 500 == 0:
        print(len(training_value))
        np.save(file_name, training_value)

main()

