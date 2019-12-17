#import imglyb 

#import numpy as np
#from skimage import data, io, filters
import imagej 
ij=imagej.init('sc.fiji:fiji')
#ij=imagej.init()
print(f'this is fijis version: ij.getVersion()')


# Import an image with scikit-image.

# NB: Blood vessel image from: https://www.fi.edu/heart/blood-vessels
img = io.imread('https://www.fi.edu/sites/fi.live.franklinds.webair.com/files/styles/featured_large/public/General_EduRes_Heart_BloodVessels_0.jpg')

img = np.mean(img, axis=2)

# Invoke ImageJ's Frangi vesselness op.
vessels = np.zeros(img.shape, dtype=img.dtype)
ij.op().filter().frangiVesselness(ij.py.to_java(vessels), ij.py.to_java(img), [1, 1], 20)



# macro='Run_QA_Portland2019'
# language_extension = 'ijm'
# result_script = ij.py.run_script(language_extension, macro)