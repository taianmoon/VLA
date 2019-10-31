#DO FIRST
#import os
#os.system('export PATH=$PATH:$HOME/Downloads/montage/bin')

import pyfits
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
import montage_wrapper as montage
from astropy.io import fits
import matplotlib.cm as cm
import aplpy


#========================================================HERE============================================


input_fits_image_band1='../H12-00_initial_clean.image.tt0_170223.fits'  #=====250
#input_fits_image_band2='./input/SGP_mf_fbacksub_350_c.fits'    #=====350
#input_fits_image_band3='./input/SGP_mf_fbacksub_500_c.fits'  #=====500
#input_fits_image_band4='./input/g018.fits'  #=====radio
#input_fits_image_band5='./input/G12v230_IRAC_Mosaic_36.fits'                            #=====3.6 micron
#input_fits_image_band6='./input/G12v230_IRAC_Mosaic_45.fits'                            #=====4.5 micron

band4_present=0  #=================================================================1:yes 0:no (I band)
band5_present=0  #=================================================================1:yes 0:no (3.6 band)
band6_present=0  #=================================================================1:yes 0:no (4.5 band)


#================================Load in fits table===============================================

#names_cutoff = pyfits.open('./G018_matches_combined.fits')                            #========================================================HERE
#names_cutoff_data = names_cutoff[1].data
#X_WORLD_K= names_cutoff_data.field('ra')
#Y_WORLD_K= names_cutoff_data.field('dec')
#K_mag = names_cutoff_data.field('f250') #==================================================HERE note to correct column name
#J_mag = names_cutoff_data.field('f350') #==================================================HERE note to correct column name
#H_mag = names_cutoff_data.field('f500') #==================================================HERE note to correct column name
#I_mag = names_cutoff_data.field('f500') #==================================================HERE note to correct column name
#NUMBER_K= names_cutoff_data.field('count') #double detection in ATCA
#NUMBER_double= names_cutoff_data.field('GroupID') #double detection in ATCA

#X_WORLD_radio= names_cutoff_data.field('col1')
#Y_WORLD_radio= names_cutoff_data.field('col2')




#===============================make a webpage showing the cutoff images============================================



#f=open('./cutoff_images.html','w+')

#f.write('<!DOCTYPE html>\n')
#f.write('<html>\n')
#f.write('<head>\n')
#f.write('\t<title>cutoff_images</title>\n')
#f.write('</head>\n')
#f.write('<body>\n')

#f.write('<table border="1">')

#f.write('<tr>')



#f.write('<td>250 micron</td>')
#f.write('<td>350 micron</td>')
#f.write('<td>500 micron</td>')

#if band4_present==1:
#    f.write('<td>5.5 GHz</td>')

#if band5_present==1:
#    f.write('<td>3.6 micron image</td>')
#if band6_present==1:
#    f.write('<td>4.5 micron image</td>')

#f.write('</tr>')

#==================to be continued in the loop=========================





try:
    montage.mSubimage(input_fits_image_band1, './output/H12-00_source30_cutout.fits', ra=176.64708, dec=-0.18040577, xsize=0.01)
except:
    print '==problem in ks image=='





#==============================do cutoff==========================================================

#for counter_cutoff in range(len(X_WORLD_K)):

#    try:
#        montage.mSubimage(input_fits_image_band1, './output/cutoff_250_'+str(NUMBER_K[counter_cutoff])+'_'+str(counter_cutoff)+'.fits', ra=X_WORLD_K[counter_cutoff], dec=Y_WORLD_K[counter_cutoff], xsize=0.05)
#    except:
#        print '==problem in ks image=='

#============================update cutoff images using aplpy=====================================================

    #cutoff_1=fits.open('./output/cutoff_ks_'+str(counter_cutoff)+'.fits')
    #cutoff_2=fits.open('./output/cutoff_j_'+str(counter_cutoff)+'.fits')
    #cutoff_3=fits.open('./output/cutoff_h_'+str(counter_cutoff)+'.fits')
    #cutoff_4=fits.open('./output/cutoff_i_'+str(counter_cutoff)+'.fits')

    #ax=plt.subplot(111)
    #ax.imshow(cutoff_1[0].data, cmap=cm.gist_heat)
    #plt.axis('off')
    #plt.savefig('./try.jpg')
    #plt.close()


    #cutoff_1.close()
    #cutoff_2.close()
    #cutoff_3.close()
    #cutoff_4.close()













