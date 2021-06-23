#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 17:55:53 2021

@author: Akash
"""
#Importing Libraries
from rasterio import plot
import pandas as pd
import numpy as np
import tensorflow as tf
import rasterio as rio
%matplotlib inline

#Loading bands
band4 = rio.open('/home/satyukt/vaari/Projects/1000/bindusen/s2/tif/B04/T43PFT_20201202T052159_B04_10m.tif')
band8 = rio.open('/home/satyukt/vaari/Projects/1000/bindusen/s2/tif/B08/T43PFT_20201202T052159_B08_10m.tif')

#to convert into ndarray
red = band4.read(1).astype('float64')
nir = band8.read(1).astype('float64')


fig = plt.figure(figsize=(18,12))
plot.show(band4)

type(ndvi)

band4.height
band8.height
band4.width
band8.width

#To generate NDVI
ndvi = np.where((nir+red) == 0,0,(nir-red)/(nir+red))

#To save NDVI
ndviImage = rio.open('/home/satyukt/Projects/test/ndvi_tensor/out/ndvi2.tiff', 'w',driver = 'Gtiff', 
                    width = band4.width, height = band4.height,count = 1,
                    crs = band4.crs, transform = band4.transform, dtype = 'float64')

ndviImage.write(ndvi,1)
ndviImage.close()

#To plot ndvi
ndvi = rio.open('/home/satyukt/Projects/test/ndvi_tensor/out/ndvi2.tiff')
fig = plt.figure(figsize=(18,12))
plot.show(ndvi)

##########################################______________________#############################################################

