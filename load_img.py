#from uqbio2021, http://q-bio.org, by Douglas Shepherd (douglas.shepherd@asu.edu) and Peter Brown (ptbrown1729@gmail.com).

############## load tiff image easily
data_fname = XX.tiff
imgs = np.squeeze(tifffile.imread(data_fname))
#print(imgs.shape)
imgs[imgs < 0] = 1e-6
img_max_proj = imgs.max(axis=0)


############## allows animated show of a time-elapse image
fig = px.imshow(imgs, x=np.linspace(0,66.5,imgs.shape[1]), y=np.linspace(0,66.5,imgs.shape[2]), 
                zmin=np.percentile(img_max_proj, 0.1), zmax=np.percentile(img_max_proj, 99.95),
                animation_frame=0, binary_string=True, labels=dict(animation_frame="slice"))
fig.show() 


############## Side-by-side comparison (when there are multiple images to display)
#Instructor: Luis U. Aguilera
#Author: Luis U. Aguilera
#Contact Info: luis.aguilera@colostate.edu
 
#Copyright (c) 2021 Dr. Brian Munsky. 
#Dr. Luis Aguilera, Will Raymond
#Colorado State University.
#Licensed under MIT License.
#fig, ax = plt.subplots(1,3, figsize=(30, 20))
ax[0].imshow(img_int3[0,:,:,0],cmap='gray') # first arg is time, last arg is color channel 
ax[0].set(title='3bit')
ax[1].imshow(img_int8[0,:,:,0],cmap='gray')
ax[1].set(title='8bit')
ax[2].imshow(img[0,:,:,0],cmap='gray')
ax[2].set(title='16bit')
plt.show()

################ thresholding 
img_copy = img.copy() # making a copy of our img
img_section = img_copy[0,:,:,0] # selecting a timepoint and color channel
#img_section[img_section>1000]=1000  # thresholding image values larger than 1000 equal to 1000.

img_section[img_section> np.mean(img_section) ]=np.mean(img_section)  # thresholding image values larger than the mean equal to the mean.


################# move in and out of focus
def FISH_viewer( z_value):
    '''
    This function is intended to display an image from an array of images (specifically, video: img_int8). img_int8 is a numpy array with dimension [T,Y,X,C].
    drop_channel : str with options 'Ch_0', 'Ch_1', 'Ch_2', 'All'
    time: int with range 0 to the number of frames in video.
    '''
    plt.figure(1)
    temp_FISH_image = img_FISH[z_value,:,:]    
    plt.imshow(temp_FISH_image,cmap='gray')
    plt.show()

# Defining an interactive plot
interactive_plot = interactive(FISH_viewer,
                               z_value = widgets.IntSlider(min=0,max=img_FISH.shape[0]-1,step=1,value=0,description='z-value'))       # time slider parameters
# Creates the controls
controls = HBox(interactive_plot.children[:-1], layout = Layout(flex_flow='row wrap'))
# Creates the outputs
output = interactive_plot.children[-1]

# Display the controls and output as an interactive widget
display(VBox([controls, output]))

