# -*- coding: utf-8 -*-
"""
Created on Sun Jul 03 15:15:46 2016

@author: SAKSHI TRIPATHI
"""

import sys
import os.path
import cv2

if __name__ == "__main__":
    
    
    ##img=cv2.imread('D:/image processing/1 (8).jpg')
    ##cv2.imshow('img',img)
    
    
    BASE_PATH='att_faces'##path of test image folder
    SEPARATOR=";"
    output=open('file.csv', 'w+')
    label = 0
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                
                abs_path = "%s/%s" % (subject_path, filename)
                ##img=cv2.imread(abs_path)
                ##cv2.imshow('img',img)
                ##cv2.waitKey(0)
                ##print("%s%s%d\n" % (abs_path, SEPARATOR, label))
                output.write("%s%s%d\n" % (abs_path, SEPARATOR, label))
            label = label + 1
    output.close()        
    
    