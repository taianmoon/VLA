import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.cm as cm
from astropy.io import fits
import astropy.wcs as wcs
from scipy.interpolate import interp1d

cluster_name='bootes1'      #==================================================================================================HERE
#cluster_centre_RA= 2.185754166694E+02      #==================================================================================================HERE
#cluster_centre_Dec= 3.555555555440E+01      #==================================================================================================HERE





hdulist = fits.open('../'+cluster_name+'/'+cluster_name+'_VLA_crop.fits')      #================================================================================HERE
w = wcs.WCS(hdulist[0].header, hdulist)
NAXIS1=hdulist[0].header['NAXIS1']
NAXIS2=hdulist[0].header['NAXIS2']
CDELT1=hdulist[0].header['CDELT1']
CDELT2=hdulist[0].header['CDELT2']
cluster_centre_RA=hdulist[0].header['CRVAL1']
cluster_centre_Dec=hdulist[0].header['CRVAL2']



scidata = hdulist[0].data
hdulist.close()




S_avg=[8.5,12.0,17.0,24.0,34.0,49.0,68.0,96.0,135.0,206.0,368.0,589.0,1084.0,1802.0,2960.0,4367.0]  #micro-Jy
S_lower=[7.0,10.0,14.0,20.0,28.0,40.0,57.0,80.0,113.0,159.0,270.0,459.0,780.0,1325.0,2249.0,3820.0]
S_upper=[10.0,14.0,20.0,28.0,40.0,57.0,80.0,113.0,159.0,270.0,459.0,780.0,1325.0,2249.0,3820.0,6487.0]


#=================================import catalogue, count sources in each bin======================================================================


template_file = open("./catalogues/"+cluster_name+"_initial_clean.image.tt0_blobs.txt", "r")    #==================================================================================================HERE

lines = template_file.readlines()
template_file.close()

response_curve=[]

for i in range(0, len(lines)):
    separated_lines=lines[i].split() 
    response_curve.append(separated_lines)


response_curve = np.array(response_curve)
flux_ujy_pre=response_curve[:,37]
RA_pre=response_curve[:,15]
Dec_pre=response_curve[:,16]


flux_ujy_pre = np.array(flux_ujy_pre)
flux_ujy_pre=np.array([float(i) for i in flux_ujy_pre])
RA_pre = np.array(RA_pre)
RA_pre=np.array([float(i) for i in RA_pre])
Dec_pre = np.array(Dec_pre)
Dec_pre=np.array([float(i) for i in Dec_pre])

flux_ujy_pre=flux_ujy_pre*1e6  #convert from Jy to micro-Jy

#print flux_ujy


flux_ujy=[]
for j in range(0, len(flux_ujy_pre)):
    if math.sqrt(pow(cluster_centre_RA - RA_pre[j], 2)+pow(cluster_centre_Dec - Dec_pre[j], 2)) <= 4.5/60.0:
        flux_ujy.append(flux_ujy_pre[j])


print flux_ujy
print 'dddddddddddddddddddddd'

#------------------binning------------------------------

#geach_flux=[3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5]  #mJy

#geach_flux_widebin=np.arange(4.0, 100.0, 2.0)


bin_number=[]
bin_number_err=[]

#flux_widebin_low=S_lower[0]
#flux_widebin_high=S_upper[0]



for j in range(0, len(S_avg)):
    counter=0.0

    #print flux_widebin_low[j]
    for i in range(0, len(flux_ujy)):

        if flux_ujy[i] >= S_lower[j] and flux_ujy[i] < S_upper[j]:
            counter=counter+1.0
    bin_number.append(counter)
    bin_number_err.append(math.sqrt(counter))

    #flux_widebin_low=flux_widebin_low+2.0
    #flux_widebin_high=flux_widebin_high+2.0

#remember to change the scatter x and err when plotting in the end!
print bin_number
print bin_number_err





#============================calculate area of the map=====================================================


#hdulist = fits.open('../'+cluster_name+'/'+cluster_name+'_VLA_crop.fits')      #================================================================================HERE
#w = wcs.WCS(hdulist[0].header, hdulist)
#NAXIS1=hdulist[0].header['NAXIS1']
#NAXIS2=hdulist[0].header['NAXIS2']
#CDELT1=hdulist[0].header['CDELT1']
#CDELT2=hdulist[0].header['CDELT2']
#CRVAL1=hdulist[0].header['CRVAL1']
#CRVAL2=hdulist[0].header['CRVAL2']

#scidata = hdulist[0].data
#hdulist.close()


pix_value_array=[]

for i in range(0, NAXIS2):
    for j in range(0, NAXIS1):
        pix_value_array.append(scidata[0,0,i,j])

pix_value_array = np.array(pix_value_array)
pix_value_array=np.array([float(i) for i in pix_value_array])

pix_value_array = pix_value_array[~np.isnan(pix_value_array)]

print len(pix_value_array), 'pixels'
print pix_value_array

#area_map=len(pix_value_array)*abs(CDELT1)*abs(CDELT2)

area_map=abs(CDELT1)*abs(CDELT2)*NAXIS1*NAXIS2

print 'the total area from flux map (deg^2) is', area_map, 'degree^2'






#=============================Calculate N_exp, expected number counts per flux bin in Euclidean space===============================


N_exp=[]


for i in range(0, len(S_avg)):

    #N_exp.append(90.0*pow(S_avg[i]/1.0e6,-2.5)*pow(math.pi/180.0,2.0)*((S_upper[i]-S_lower[i])/1.0e6)*area_map)
    N_exp.append(90.0*pow(S_avg[i]/1.0e6,-2.5)*pow(math.pi/180.0,2.0)*((S_upper[i]-S_lower[i])/1.0e6)*math.pi*pow(4.5/60.0, 2))

print N_exp
print 'xxxxxxxxxxxxxxxx'




#==========================Calculate the effective cumulative area from the sensitivity map===========================================
#
#
#hdulist_noise = fits.open('../'+cluster_name+'/'+cluster_name+'_VLA_rms_crop.fits')      #================================================================================HERE
#w_noise = wcs.WCS(hdulist_noise[0].header, hdulist_noise)
#NAXIS1_noise=hdulist_noise[0].header['NAXIS1']
#NAXIS2_noise=hdulist_noise[0].header['NAXIS2']
#CDELT1_noise=hdulist_noise[0].header['CDELT1']
#CDELT2_noise=hdulist_noise[0].header['CDELT2']
#BMAJ=hdulist_noise[0].header['BMAJ']
#BMIN=hdulist_noise[0].header['BMIN']
#scidata_noise = hdulist_noise[0].data
#hdulist_noise.close()
#
#
#pixel_per_beam = math.pi*BMAJ*BMIN/(CDELT1_noise*CDELT2_noise)
#print pixel_per_beam
#print 'ddddddddddddddddddddd'
#
#noise_value_array=[]
#
#for i in range(0, NAXIS2_noise):
#    for j in range(0, NAXIS1_noise):
#        noise_value_array.append(math.sqrt(scidata_noise[i,j]))   #Orz ([i,j] for S2CLS; [0,i,j] for ordinary fields)
#
#
#noise_value_array = np.array(noise_value_array)
#noise_value_array=np.array([float(i) for i in noise_value_array])  #(wavelength in angstrom)
#
#noise_value_array = noise_value_array[~np.isnan(noise_value_array)]
#
#
#noise_value_array_sorted= sorted(noise_value_array)
#
#
#noise_value_array_sorted = np.array(noise_value_array_sorted)
#noise_value_array_sorted=np.array([float(i) for i in noise_value_array_sorted])  #(wavelength in angstrom)
#
#
#
#noise_value_array_sorted=noise_value_array_sorted*5.0/abs(pixel_per_beam) #============================================HERE: detection threshold 5-sigma for VLA? then divide pixel/beam to get Jy/pixel
#
##print 'the faintest sensitivity (mJy) is ', noise_value_array_sorted[0]
#
#noise_area=[]
#noise_pix_counter=0.0
#for i in range(0, len(noise_value_array_sorted)):
#    noise_pix_counter=noise_pix_counter+1.0
#    noise_area.append(noise_pix_counter*abs(CDELT1_noise)*abs(CDELT2_noise))    #area in deg^2
#
#
#
##print noise_value_array_sorted
##print noise_area
#
##multiply_factor=math.pi*pow(4.5/60, 2)/noise_area
#
#multiply_factor=[]
#for kk in range(0, len(S_avg)):
#    multiply_factor.append((math.pi*pow(4.5/60, 2))/np.interp(S_avg[kk]*1e-6, noise_value_array_sorted, noise_area))
#    #if np.interp(S_avg[kk]*1e-6, noise_value_array_sorted, noise_area) >= 0.01:
#    #    multiply_factor.append((math.pi*pow(4.5/60, 2))/np.interp(S_avg[kk]*1e-6, noise_value_array_sorted, noise_area))
#    #else:
#    #    multiply_factor.append((math.pi*pow(4.5/60, 2))/0.01)
#
#multiply_factor=np.array(multiply_factor)
#
#

#========================Calculate Nc/Nexp, and its error=============================================================================


Nc_Nexp=[]
Nc_Nexp_err=[]

for i in range(0, len(bin_number)):

    Nc_Nexp.append(bin_number[i]/N_exp[i])
    #Nc_Nexp_err.append(bin_number[i]/(N_exp[i]*math.sqrt(bin_number[i])))
    Nc_Nexp_err.append(math.sqrt(bin_number[i])/N_exp[i])


Nc_Nexp = np.array(Nc_Nexp)
Nc_Nexp=np.array([float(i) for i in Nc_Nexp])
Nc_Nexp_err = np.array(Nc_Nexp_err)
Nc_Nexp_err=np.array([float(i) for i in Nc_Nexp_err])


Nc_Nexp=Nc_Nexp*1.0e2   #1.0e-2
Nc_Nexp_err=Nc_Nexp_err*1.0e2   #1.0e-2

print Nc_Nexp
print Nc_Nexp_err


mock_catalogue=np.column_stack((Nc_Nexp, Nc_Nexp_err))
np.savetxt('./190802/ncounts_'+cluster_name+'.cat', mock_catalogue, delimiter=' ') #================================================================================HERE

#========================Plotting==============================================================================================================




#literature data
Nc_Nexp_literature=[0.0,0.0,0.0,0.0,0.0,0.85,0.91,1.35,1.25,1.46,1.6,4.96,5.25,7.2,14.45,11.11]  #1.0e-2
Nc_Nexp_literature_err=[0.0,0.0,0.0,0.0,0.0,0.2,0.25,0.25,0.29,0.33,0.51,1.28,2.07,3.47,7.01,7.58]  #1.0e-2






plt.scatter(S_avg, Nc_Nexp_literature, color='r', label='Huynh et al. (2015)', s=100)
plt.errorbar(S_avg, Nc_Nexp_literature, yerr=Nc_Nexp_literature_err, color='r', fmt='o', elinewidth=2.0, capsize=4.0, capthick=2.0) 

plt.scatter(S_avg, Nc_Nexp, color='b', label='this work', s=100, marker='s') 
plt.errorbar(S_avg, Nc_Nexp, yerr=Nc_Nexp_err, color='b', fmt='o', elinewidth=2.0, capsize=4.0, capthick=2.0) 






plt.grid()
plt.xscale('log',nonposy='clip')
plt.yscale('log',nonposy='clip')
plt.xlabel(r'$S(6cm)$ [$\mu$Jy]')
plt.ylabel(r'$N_c/N_{exp}$ [1x$10^{-2}$]')
plt.rc('font', size=30) 
plt.legend(loc=2)
plt.title(cluster_name)   #======================================================================================================================================HERE
plt.show()






