#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:45:05 2020

@author: sudhanshukumar
"""
import mahotas as mh
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import seaborn as sns
from matplotlib import pyplot as plt 
from glob import glob

import pickle
def diagnosis(file):
    # Download image
    ##YOUR CODE GOES HERE##
    try:
        image = mh.imread(file)
    except:
        print("Cannot download image: ", file)
        return
        
    # Prepare image to classification
    ##YOUR CODE GOES HERE##
    IMM_SIZE = 224

    if len(image.shape) > 2:
        image = mh.resize_to(image, [IMM_SIZE, IMM_SIZE, image.shape[2]]) #resize of images RGB and png
    else:
        image = mh.resize_to(image, [IMM_SIZE, IMM_SIZE]) #resize of grey images    
    if len(image.shape) > 2:
        image = mh.colors.rgb2grey(image[:,:,:3], dtype = np.uint8)  #change of colormap of images alpha chanel delete
         
    # Show image
    ##YOUR CODE GOES HERE##

   
    
    # Load model  
    ##YOUR CODE GOES HERE##

    from keras.models import model_from_json
    json_file = open('C:\\Users\\dell\\Desktop\\x-ray\\model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("C:\\Users\\dell\\Desktop\\x-ray\\model.h5")        
    with open('C:\\Users\\dell\\Desktop\\x-ray\\history.pickle', 'rb') as f:
        history = pickle.load(f)
    with open('C:\\Users\\dell\\Desktop\\x-ray\\lab.pickle', 'rb') as f:
        lab = pickle.load(f)
    # Normalize the data
    ##YOUR CODE GOES HERE##

    image = np.array(image) / 255
    # Reshape input images
    ##YOUR CODE GOES HERE##

    image = image.reshape(-1, IMM_SIZE, IMM_SIZE, 1)
    # Predict the diagnosis
    ##YOUR CODE GOES HERE##
    
    predict_x=model.predict(image) 
    diag=np.argmax(predict_x,axis=1)
    # Find the name of the diagnosis  
    ##YOUR CODE GOES HERE##
    diag =list(lab.keys())[list(lab.values()).index(diag[0])]

    
    return diag