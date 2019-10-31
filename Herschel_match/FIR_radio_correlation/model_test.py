import matplotlib.pyplot as plt
import numpy as np
import math
#import matplotlib.cm as cm
#from astropy.io import fits
#import astropy.wcs as wcs
#from scipy.interpolate import interp1d
#import pyfits
#import os
#import subprocess



flux_6gz=np.arange(1.0e-5, 1.0e-4, 5.0e-7)  #========================================================HERE: 10-100 uJy (unit in Jy)

#print flux_6gz


flux_350=[]  #in Jy

for i in range(0,len(flux_6gz)):

    flux_350.append(1.167e-12*pow(10.0,2.5)*3.75e12*pow(6.0/1.4,0.8)*flux_6gz[i])


#print flux_350

flux_6gz = np.array(flux_6gz)
flux_6gz=np.array([float(i) for i in flux_6gz])
flux_350 = np.array(flux_350)
flux_350=np.array([float(i) for i in flux_350])

flux_6gz_ujy=flux_6gz*1.0e6
flux_350_mjy=flux_350*1000.0


plt.plot(flux_350_mjy, flux_6gz_ujy)

plt.xscale('log', nonposx='clip')
plt.yscale('log', nonposy='clip')

plt.grid()
plt.xlabel('F350 (mJy)')  #==========================================================HERE
plt.ylabel('6 GHz flux (uJy)')  #==========================================================HERE
plt.rc('font', size=30)
plt.show()

