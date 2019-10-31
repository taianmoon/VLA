##import matplotlib.pyplot as plt
#import numpy as np
#import math
##import matplotlib.cm as cm
#from astropy.io import fits
#import astropy.wcs as wcs



#cut_radius = 350.0  #==============HERE: in arcsec



#hdulist = fits.open('../'+cluster_list[l]+'/Blobcat_source_detection/sextractor_noise/rms_noise.fits')      #========================================================================HERE
hdulist = fits.open('../'+cluster_list[l]+'/'+cluster_list[l]+'_VLA_rms_crop.fits')      #========================================================================HERE
w_flux = wcs.WCS(hdulist[0].header, hdulist)
NAXIS1_flux=hdulist[0].header['NAXIS1']
NAXIS2_flux=hdulist[0].header['NAXIS2']
CDELT1_flux=hdulist[0].header['CDELT1']
CDELT2_flux=hdulist[0].header['CDELT2']
CRPIX1_flux=hdulist[0].header['CRPIX1']
CRPIX2_flux=hdulist[0].header['CRPIX2']
CRVAL1_flux=hdulist[0].header['CRVAL1']
CRVAL2_flux=hdulist[0].header['CRVAL2']

scidata_flux = hdulist[0].data
header_flux = hdulist[0].header


hdulist.close()


#print scidata_flux[0,0,4100:4300, 4100:4300]

#header_flux['NAXIS'] =4  #=================================HERE: uncomment when it's flux map!!!



#for i in range(0, NAXIS2_flux):
#    for j in range(0, NAXIS1_flux):
#        if np.sqrt(pow(j-(CRPIX1_flux-1.0), 2)+pow(i-(CRPIX2_flux-1.0), 2)) >= (cut_radius/3600.0)/abs(CDELT1_flux):
#            scidata_flux[i, j] = 'nan'  #=================================================================================================HERE: check, depends

#print scidata_flux[0, 100, :]


hdu = fits.PrimaryHDU(scidata_flux[4100:4300, 4100:4300], header=header_flux)  #[0,0, xxx, xxx] for flux map!!!!
hdul = fits.HDUList([hdu])

hdul.writeto('../'+cluster_list[l]+'/'+cluster_list[l]+'_crop_rms_sqaure_small.fits')
















#hdulist.writeto('../'+cluster_list[l]+'/'+cluster_list[l]+'_VLA_rms_crop.fits')




#hdulist.close()

























