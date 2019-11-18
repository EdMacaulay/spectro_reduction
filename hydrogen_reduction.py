# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:07:41 2019
Reducing science frame of hydrogen lamp

@author: Lani Chastain
"""

from astropy.io import fits
from astropy import units as u
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
from astropy.visualization import quantity_support

# Import science frame and extract the data from the PRIMARY row. 
# Note: the directory path will be different based on where the file is located on the computer

hdu_list = fits.open(r"C:\Users\14238\Downloads\CosmoCrew\science.fits\CCD_Image_6.fit")
hdu_list.info()
sciencedata = hdu_list[0].data
hdu_list.close()

# Plot the data using a log scale to increase the "brightness" of the image

plt.imshow(sciencedata)
plt.imshow(np.log10(sciencedata))

# Import the bias frame

bias_list = fits.open(r"C:\Users\14238\Downloads\CosmoCrew\bias.fits\CCD_Image_11.fit")
bias_list.info()
biasdata = bias_list[0].data
bias_list.close()

# Subtract the bias frame from the science frame using element-by-element array subtraction

subtracted_science = np.subtract(hdu_list[0].data,bias_list[0].data)
plt.imshow(subtracted_science)
plt.show()

# Import Flat frame

flat_list = fits.open(r"C:\Users\14238\Downloads\CosmoCrew\flats.fits\CCD_Image_35.fit")
flat_list.info()
flatdata = flat_list[0].data
flat_list.close()

# Divide the subtracted frame by the flat

divided_science = np.divide(subtracted_science,flatdata)
plt.imshow(divided_science)
plt.imshow(np.log10(divided_science))
plt.show()

# Plot the emission values of the reduced frame 
plt.plot(divided_science[:,450]) 
plt.show()
# Plot the sum of the values from columns 450-550
plt.plot(np.sum(divided_science[:,450:550],axis=1))
plt.show()

# Plot the science frame without dividing by the flat to produce a graph without the
# effects of the uneven flat frame
plt.plot(np.sum(subtracted_science[:,450:550],axis=1))
plt.show()
