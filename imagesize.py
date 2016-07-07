# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 23:27:30 2016

@author: SAKSHI TRIPATHI
"""

import sys
import os.path
import cv2
from PIL import Image

if __name__ == "__main__":


    ##img=cv2.imread('D:/image processing/1 (8).jpg')
    ##cv2.imshow('img',img)


    BASE_PATH='C:/Users/SAKSHI TRIPATHI/Downloads/Face_recog_LBPH-master/Face_recog_LBPH-master/FACES_self_dataset'
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):

                abs_path = "%s/%s" % (subject_path, filename)
                img=cv2.imread(abs_path)
                dim=(59,59)
                img=cv2.resize(img,dim)
                ##cv2.imshow('cropped',img)
                ##cv2.waitKey(0)
                cv2.imwrite(abs_path,img)
