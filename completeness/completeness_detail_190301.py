#import matplotlib.pyplot as plt
#import numpy as np
#import math
#import matplotlib.cm as cm
#from astropy.io import fits
#import astropy.wcs as wcs
#from scipy.interpolate import interp1d
#import random



#hdulist_flux = fits.open('../'+cluster_list[l]+'/'+cluster_list[l]+'_VLA_crop.fits')      #================================================================================HERE
hdulist_flux = fits.open('../'+cluster_list[l]+'/'+cluster_list[l]+'_crop_sqaure_small.fits')      #================================================================================HERE
w_flux = wcs.WCS(hdulist_flux[0].header, hdulist_flux)
NAXIS1_flux=hdulist_flux[0].header['NAXIS1']
NAXIS2_flux=hdulist_flux[0].header['NAXIS2']
CDELT1_flux=hdulist_flux[0].header['CDELT1']
CDELT2_flux=hdulist_flux[0].header['CDELT2']
scidata_flux = hdulist_flux[0].data  #================flux: unit of pW
hdr = hdulist_flux[0].header
hdulist_flux.close()


#print scidata_flux[0, 100, 100]


random_positions_x_long=[]
random_positions_y_long=[]
while len(random_positions_x_long) < number_of_sources:
#for i in range(100):   #==============================================================================choose intial random position number: HERE
    x_tmp=random.randint(1,NAXIS1_flux)
    y_tmp=random.randint(1,NAXIS2_flux)
    if sensitivity_switch==1:
        if math.sqrt(pow(x_tmp-(NAXIS1_flux/2.0), 2.0)+pow(y_tmp-(NAXIS2_flux/2.0), 2.0)) <= radius_sources/(60.0*abs(CDELT1_flux)) and np.isnan(scidata_flux[y_tmp, x_tmp])==False:
            random_positions_x_long.append(x_tmp)
            random_positions_y_long.append(y_tmp)

    else:
        if np.isnan(scidata_flux[y_tmp, x_tmp])==False:
            random_positions_x_long.append(x_tmp)
            random_positions_y_long.append(y_tmp)

random_positions_x = random_positions_x_long[0:number_of_sources]
random_positions_y = random_positions_y_long[0:number_of_sources]

#print random_positions_x
#print random_positions_y


#print random_positions_x
#print random_positions_y
#print len(random_positions_x)
#print len(random_positions_y)
#print '1111111111111111111111'



#random_flux=[2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]*1.0e-3/537.0 #mJy--> pW
#random_flux=10.0*1.0e-3/537.0 #mJy--> pW



for i in range (0, len(random_positions_x)):  #=================loop over 10 random positions, specify their flux values
    if np.isnan(scidata_flux[random_positions_y[i], random_positions_x[i]])==False:
        scidata_flux[ random_positions_y[i], random_positions_x[i]]=random_flux[rf]  #peak (central) pixel of 2D-Gaussian
        
        for pvx in range(0,5):
            for pvy in range(0,5):
        
                scidata_flux[random_positions_y[i]+pvx, random_positions_x[i]+pvy]=two_d_gaussian(random_flux[rf], random_positions_y[i], random_positions_x[i], random_positions_y[i]+pvx, random_positions_x[i]+pvy, abs(CDELT2_flux), abs(CDELT1_flux))
                scidata_flux[ random_positions_y[i]-pvx, random_positions_x[i]-pvy]=two_d_gaussian(random_flux[rf], random_positions_y[i], random_positions_x[i], random_positions_y[i]-pvx, random_positions_x[i]-pvy, abs(CDELT2_flux), abs(CDELT1_flux))
                scidata_flux[ random_positions_y[i]+pvx, random_positions_x[i]-pvy]=two_d_gaussian(random_flux[rf], random_positions_y[i], random_positions_x[i], random_positions_y[i]+pvx, random_positions_x[i]-pvy, abs(CDELT2_flux), abs(CDELT1_flux))
                scidata_flux[ random_positions_y[i]-pvx, random_positions_x[i]+pvy]=two_d_gaussian(random_flux[rf], random_positions_y[i], random_positions_x[i], random_positions_y[i]-pvx, random_positions_x[i]+pvy, abs(CDELT2_flux), abs(CDELT1_flux))




        #scidata_flux[0, random_positions_y[i]+1, random_positions_x[i]]=random_flux[rf]
        #scidata_flux[0, random_positions_y[i], random_positions_x[i]+1]=random_flux[rf]
        #scidata_flux[0, random_positions_y[i]-1, random_positions_x[i]]=random_flux[rf]
        #scidata_flux[0, random_positions_y[i], random_positions_x[i]-1]=random_flux[rf]
        #print scidata_flux[0, random_positions_y[i], random_positions_x[i]]


hdu = fits.PrimaryHDU(scidata_flux[:,:], header=hdr)
hdul = fits.HDUList([hdu])

hdul.writeto('./output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_flux_170919.fits')



#hdulist_noise_2 = fits.open('./'+cluster_list[l]+'/'+cluster_list[l]+'_flux_170919.fits')      #================================================================================HERE
#w_noise_2 = wcs.WCS(hdulist_noise_2[1].header, hdulist_noise_2)
#NAXIS1_noise=hdulist_noise_2[1].header['NAXIS1']
#NAXIS2_noise=hdulist_noise_2[1].header['NAXIS2']
#CDELT1_noise=hdulist_noise_2[1].header['CDELT1']
#CDELT2_noise=hdulist_noise_2[1].header['CDELT2']
#scidata_noise_2 = np.sqrt(hdulist_noise_2[1].data)  #================variance: unit of pW
#hdulist_noise_2.close()

sn_ratio=scidata_flux[:,:]/scidata_noise_2

hdu_sn = fits.PrimaryHDU(sn_ratio, header=hdr)
hdul_sn = fits.HDUList([hdu_sn])

hdul_sn.writeto('./output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_snr_170919.fits')





