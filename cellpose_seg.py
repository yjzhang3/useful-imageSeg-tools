""" Instructor: Zachary Fox
Author: Zachary Fox
Contact Info: zachfox@lanl.gov
 
Copyright (c) 2021 Dr. Brian Munsky. 
Dr. Luis Aguilera, Will Raymond
Colorado State University.
Licensed under MIT License.
"""

""" Live Tutorial 1a – Single-cell segmentation in Python (Zach Fox) """

%matplotlib inline
import skimage as sk
import numpy as np
import urllib.request 
import matplotlib.pyplot as plt
from skimage.io import imread 

############### import tiff files
figName = XXX.tif
images = sk.io.imread(figName) 

############### load into an array
img = images[0,:,:,0]
f,ax = plt.subplots()
ax.imshow(img, cmap='Greys')

############### use histogram to look at pixel density distribution
!pip install cellpose
from cellpose import models
from cellpose import plot

use_GPU = models.use_gpu()

# DEFINE CELLPOSE MODEL
model = models.Cellpose(gpu=use_GPU, model_type='cyto') # model_type='cyto' or model_type='nuclei'

# Running the models
masks, flows, styles, diams = model.eval(img, diameter=200, flow_threshold=None, channels=[0,0])

plt.imshow(masks,cmap='Greys')
plt.show()
