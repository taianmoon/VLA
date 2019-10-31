#import matplotlib.pyplot as plt
import numpy as np
import math
#import matplotlib.cm as cm
from astropy.io import fits
import astropy.wcs as wcs


cut_radius = 270.0  #==============HERE: in arcsec



cluster_list=['bootes1', 'H12-00', 'Lockman1', 'NGP1', 'NGP3', 'NGP5', 'NGP6', 'NGP7', 'NGP9']
#cluster_list=['bootes1']




for l in range (0, len(cluster_list)):  #=================loop over realization times
    
    print l
    print cluster_list[l]
    #execfile("./cutout_circle_190503.py")
    execfile("./cutout_square_191021.py")
