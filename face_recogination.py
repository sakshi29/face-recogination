# -*- coding: utf-8 -*-
"""
Created on Sun Jul 03 19:34:06 2016

@author: SAKSHI TRIPATHI
"""

import cv2
import numpy

import csv


def train_data(label):
    
    model = cv2.createEigenFaceRecognizer()
    model.train(label.values(), numpy.array(label.keys()))
    return model

def predict_image(model, image):
    
    return model.predict(image)

def read_csvfile(filename='file.csv'):
    
    csv = open(filename, 'r')
    return csv

def get_training_data(file):
    
    lines = file.readlines()
    training_data= lines
    ##print training_data
    return training_data

def create_label_matrix_dict(input_file):
    
    label_dict = {}
    ##print len(input_file)
    
    for line in input_file :
        ## split on the ';' in the csv separating filename;label
        ##print line
        
        filename, label= line.strip().split(';')

        ##update the current key if it exists, else append to it
        if label_dict.has_key(int(label)):
            current_files = label_dict.get(label)
            numpy.append(current_files,read_image(filename))
        else:
            label_dict[int(label)] = read_image(filename)
       
    return label_dict 


    
def read_image(filename):
     
     return cv2.imread(filename, cv2.CV_LOAD_IMAGE_GRAYSCALE)
     ##img=cv2.imread('D:/image procesing/att_faces/s4/8.pgm')
     ##cv2.imshow(img)
     ##cv2.waitKey(0)
     
     
if __name__ == "__main__":
    training_data = get_training_data(read_csvfile())
    ##print len(training_data)
    dataindex= create_label_matrix_dict(training_data)
    model = train_data(dataindex) 
    
    line='1.pgm'
    ##line image u want to search for
    
    predicted_label = predict_image(model, read_image(line))
    
    print 'Predicted: %(predicted)s ' %  {"predicted": predicted_label[0]}
    
    ##for imagepath in glob.glob('D:/image processing/att_faces//*'):
    with open('file.csv','rb') as f:
        read=csv.reader(f)
        for i in read:
            img,lab=i[0].split(";")
            
            ##print img
            
            if(int(lab)==predicted_label[0]):
                ##print 'hey'
                result=cv2.imread(img)
                cv2.imshow('img',result)
                cv2.waitKey(0)
              
##cv2.destroyAllWindow()                             