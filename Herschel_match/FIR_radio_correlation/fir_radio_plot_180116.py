import pyfits
import matplotlib.pyplot as plt
import numpy as np
import math
import glob
import os.path


#----------------Bootes1

names_wht_bootes1 = pyfits.open('../Bootes1_VLA_Herschel_match.fits')                            #========================================================HERE
names_wht_data = names_wht_bootes1[1].data
names_wht_bootes1.close()

#flux_250= names_wht_data.field('F250')    #========================================================HERE(Bootes: F250, et_F250; EGS/NGP9: f250, et250; G12/NGP: F250, E250)
#error_250= names_wht_data.field('et_f250')    #========================================================HER
flux_350_bootes1= names_wht_data.field('F350')    #========================================================HER
error_350_bootes1= names_wht_data.field('et_f350')    #========================================================HER
#flux_500= names_wht_data.field('F500')    #========================================================HER
#error_500= names_wht_data.field('et_f500')    #========================================================HER
flux_radio_bootes1= names_wht_data.field('col38')
error_radio_bootes1= names_wht_data.field('col39')



#flux_250 = np.array(flux_250)
#flux_250=np.array([float(i) for i in flux_250])
#error_250 = np.array(error_250)
#error_250=np.array([float(i) for i in error_250])
flux_350_bootes1 = np.array(flux_350_bootes1)
flux_350_bootes1=np.array([float(i) for i in flux_350_bootes1])
error_350_bootes1 = np.array(error_350_bootes1)
error_350_bootes1=np.array([float(i) for i in error_350_bootes1])
#flux_500 = np.array(flux_500)
#flux_500=np.array([float(i) for i in flux_500])
#error_500 = np.array(error_500)
#error_500=np.array([float(i) for i in error_500])
flux_radio_bootes1 = np.array(flux_radio_bootes1)
flux_radio_bootes1=np.array([float(i) for i in flux_radio_bootes1])
error_radio_bootes1 = np.array(error_radio_bootes1)
error_radio_bootes1=np.array([float(i) for i in error_radio_bootes1])

#print error_radio_bootes1

#----------------G12

names_wht_g12 = pyfits.open('../G12_VLA_Herschel_match.fits')                            #========================================================HERE
names_wht_data = names_wht_g12[1].data
names_wht_g12.close()


flux_350_g12= names_wht_data.field('F350')    #========================================================HER
error_350_g12= names_wht_data.field('e350')    #========================================================HER
flux_radio_g12= names_wht_data.field('col38')
error_radio_g12= names_wht_data.field('col39')

flux_350_g12 = np.array(flux_350_g12)
flux_350_g12=np.array([float(i) for i in flux_350_g12])
error_350_g12 = np.array(error_350_g12)
error_350_g12=np.array([float(i) for i in error_350_g12])
flux_radio_g12 = np.array(flux_radio_g12)
flux_radio_g12=np.array([float(i) for i in flux_radio_g12])
error_radio_g12 = np.array(error_radio_g12)
error_radio_g12=np.array([float(i) for i in error_radio_g12])

flux_350_g12=flux_350_g12*1000.0
error_350_g12=error_350_g12*1000.0



#-----------------Lockman

names_wht_lockman = pyfits.open('../Lockman_VLA_Herschel_match.fits')                            #========================================================HERE
names_wht_data = names_wht_lockman[1].data
names_wht_lockman.close()


flux_350_lockman= names_wht_data.field('F350')    #========================================================HER
error_350_lockman= names_wht_data.field('et350')    #========================================================HER
flux_radio_lockman= names_wht_data.field('col38')
error_radio_lockman= names_wht_data.field('col39')

flux_350_lockman = np.array(flux_350_lockman)
flux_350_lockman=np.array([float(i) for i in flux_350_lockman])
error_350_lockman = np.array(error_350_lockman)
error_350_lockman=np.array([float(i) for i in error_350_lockman])
flux_radio_lockman = np.array(flux_radio_lockman)
flux_radio_lockman=np.array([float(i) for i in flux_radio_lockman])
error_radio_lockman = np.array(error_radio_lockman)
error_radio_lockman=np.array([float(i) for i in error_radio_lockman])


#---------------NGP1

names_wht_ngp1 = pyfits.open('../NGP1_VLA_Herschel_match.fits')                            #========================================================HERE
names_wht_data = names_wht_ngp1[1].data
names_wht_ngp1.close()


flux_350_ngp1= names_wht_data.field('F350')    #========================================================HER
error_350_ngp1= names_wht_data.field('e350')    #========================================================HER
flux_radio_ngp1= names_wht_data.field('col38')
error_radio_ngp1= names_wht_data.field('col39')

flux_350_ngp1 = np.array(flux_350_ngp1)
flux_350_ngp1=np.array([float(i) for i in flux_350_ngp1])
error_350_ngp1 = np.array(error_350_ngp1)
error_350_ngp1=np.array([float(i) for i in error_350_ngp1])
flux_radio_ngp1 = np.array(flux_radio_ngp1)
flux_radio_ngp1=np.array([float(i) for i in flux_radio_ngp1])
error_radio_ngp1 = np.array(error_radio_ngp1)
error_radio_ngp1=np.array([float(i) for i in error_radio_ngp1])

flux_350_ngp1=flux_350_ngp1*1000.0
error_350_ngp1=error_350_ngp1*1000.0



#-----------------NGP3

names_wht_ngp3 = pyfits.open('../NGP3_VLA_Herschel_match.fits')                            #========================================================HERE
names_wht_data = names_wht_ngp3[1].data
names_wht_ngp3.close()


flux_350_ngp3= names_wht_data.field('F350')    #========================================================HER
error_350_ngp3= names_wht_data.field('e350')    #========================================================HER
flux_radio_ngp3= names_wht_data.field('col38')
error_radio_ngp3= names_wht_data.field('col39')

flux_350_ngp3 = np.array(flux_350_ngp3)
flux_350_ngp3=np.array([float(i) for i in flux_350_ngp3])
error_350_ngp3 = np.array(error_350_ngp3)
error_350_ngp3=np.array([float(i) for i in error_350_ngp3])
flux_radio_ngp3 = np.array(flux_radio_ngp3)
flux_radio_ngp3=np.array([float(i) for i in flux_radio_ngp3])
error_radio_ngp3 = np.array(error_radio_ngp3)
error_radio_ngp3=np.array([float(i) for i in error_radio_ngp3])

flux_350_ngp3=flux_350_ngp3*1000.0
error_350_ngp3=error_350_ngp3*1000.0

#----------------NGP5

names_wht_ngp5 = pyfits.open('../NGP5_VLA_Herschel_match.fits')                            #========================================================HERE
names_wht_data = names_wht_ngp5[1].data
names_wht_ngp5.close()


flux_350_ngp5= names_wht_data.field('F350')    #========================================================HER
error_350_ngp5= names_wht_data.field('e350')    #========================================================HER
flux_radio_ngp5= names_wht_data.field('col38')
error_radio_ngp5= names_wht_data.field('col39')

flux_350_ngp5 = np.array(flux_350_ngp5)
flux_350_ngp5=np.array([float(i) for i in flux_350_ngp5])
error_350_ngp5 = np.array(error_350_ngp5)
error_350_ngp5=np.array([float(i) for i in error_350_ngp5])
flux_radio_ngp5 = np.array(flux_radio_ngp5)
flux_radio_ngp5=np.array([float(i) for i in flux_radio_ngp5])
error_radio_ngp5 = np.array(error_radio_ngp5)
error_radio_ngp5=np.array([float(i) for i in error_radio_ngp5])

flux_350_ngp5=flux_350_ngp5*1000.0
error_350_ngp5=error_350_ngp5*1000.0

#--------------------------NGP6

names_wht_ngp6 = pyfits.open('../NGP6_VLA_Herschel_match.fits')                            #========================================================HERE
names_wht_data = names_wht_ngp6[1].data
names_wht_ngp6.close()


flux_350_ngp6= names_wht_data.field('F350')    #========================================================HER
error_350_ngp6= names_wht_data.field('e350')    #========================================================HER
flux_radio_ngp6= names_wht_data.field('col38')
error_radio_ngp6= names_wht_data.field('col39')

flux_350_ngp6 = np.array(flux_350_ngp6)
flux_350_ngp6=np.array([float(i) for i in flux_350_ngp6])
error_350_ngp6 = np.array(error_350_ngp6)
error_350_ngp6=np.array([float(i) for i in error_350_ngp6])
flux_radio_ngp6 = np.array(flux_radio_ngp6)
flux_radio_ngp6=np.array([float(i) for i in flux_radio_ngp6])
error_radio_ngp6 = np.array(error_radio_ngp6)
error_radio_ngp6=np.array([float(i) for i in error_radio_ngp6])

flux_350_ngp6=flux_350_ngp6*1000.0
error_350_ngp6=error_350_ngp6*1000.0

#------------------------NGP7

names_wht_ngp7 = pyfits.open('../NGP7_VLA_Herschel_match.fits')                            #========================================================HERE
names_wht_data = names_wht_ngp7[1].data
names_wht_ngp7.close()


flux_350_ngp7= names_wht_data.field('F350')    #========================================================HER
error_350_ngp7= names_wht_data.field('e350')    #========================================================HER
flux_radio_ngp7= names_wht_data.field('col38')
error_radio_ngp7= names_wht_data.field('col39')

flux_350_ngp7 = np.array(flux_350_ngp7)
flux_350_ngp7=np.array([float(i) for i in flux_350_ngp7])
error_350_ngp7 = np.array(error_350_ngp7)
error_350_ngp7=np.array([float(i) for i in error_350_ngp7])
flux_radio_ngp7 = np.array(flux_radio_ngp7)
flux_radio_ngp7=np.array([float(i) for i in flux_radio_ngp7])
error_radio_ngp7 = np.array(error_radio_ngp7)
error_radio_ngp7=np.array([float(i) for i in error_radio_ngp7])

flux_350_ngp7=flux_350_ngp7*1000.0
error_350_ngp7=error_350_ngp7*1000.0

#------------------------NGP9

names_wht_ngp9 = pyfits.open('../NGP9_VLA_Herschel_match.fits')                            #========================================================HERE
names_wht_data = names_wht_ngp9[1].data
names_wht_ngp9.close()


flux_350_ngp9= names_wht_data.field('F350')    #========================================================HER
error_350_ngp9= names_wht_data.field('e350')    #========================================================HER
flux_radio_ngp9= names_wht_data.field('col38')
error_radio_ngp9= names_wht_data.field('col39')

flux_350_ngp9 = np.array(flux_350_ngp9)
flux_350_ngp9=np.array([float(i) for i in flux_350_ngp9])
error_350_ngp9 = np.array(error_350_ngp9)
error_350_ngp9=np.array([float(i) for i in error_350_ngp9])
flux_radio_ngp9 = np.array(flux_radio_ngp9)
flux_radio_ngp9=np.array([float(i) for i in flux_radio_ngp9])
error_radio_ngp9 = np.array(error_radio_ngp9)
error_radio_ngp9=np.array([float(i) for i in error_radio_ngp9])

flux_350_ngp9=flux_350_ngp9*1000.0
error_350_ngp9=error_350_ngp9*1000.0


#------------------------G018 (ATCA)

names_wht_g018 = pyfits.open('../G018_ATCA_Herschel_match.fits')                            #========================================================HERE
names_wht_data = names_wht_g018[1].data
names_wht_g018.close()


flux_350_g018= names_wht_data.field('F350')    #========================================================HER
error_350_g018= names_wht_data.field('e350')    #========================================================HER
flux_radio_g018= names_wht_data.field('col38')
error_radio_g018= names_wht_data.field('col39')

flux_350_g018 = np.array(flux_350_g018)
flux_350_g018=np.array([float(i) for i in flux_350_g018])
error_350_g018 = np.array(error_350_g018)
error_350_g018=np.array([float(i) for i in error_350_g018])
flux_radio_g018 = np.array(flux_radio_g018)
flux_radio_g018=np.array([float(i) for i in flux_radio_g018])
error_radio_g018 = np.array(error_radio_g018)
error_radio_g018=np.array([float(i) for i in error_radio_g018])

flux_350_g018=flux_350_g018*1000.0
error_350_g018=error_350_g018*1000.0



#---------------------------------------------------------------------

flux_radio_bootes1= flux_radio_bootes1*1.0e6
error_radio_bootes1= error_radio_bootes1*1.0e6


flux_radio_g12= flux_radio_g12*1.0e6
error_radio_g12= error_radio_g12*1.0e6

flux_radio_lockman= flux_radio_lockman*1.0e6
error_radio_lockman= error_radio_lockman*1.0e6

flux_radio_ngp1= flux_radio_ngp1*1.0e6
error_radio_ngp1= error_radio_ngp1*1.0e6

flux_radio_ngp3= flux_radio_ngp3*1.0e6
error_radio_ngp3= error_radio_ngp3*1.0e6

flux_radio_ngp5= flux_radio_ngp5*1.0e6
error_radio_ngp5= error_radio_ngp5*1.0e6

flux_radio_ngp6= flux_radio_ngp6*1.0e6
error_radio_ngp6= error_radio_ngp6*1.0e6

flux_radio_ngp7= flux_radio_ngp7*1.0e6
error_radio_ngp7= error_radio_ngp7*1.0e6

flux_radio_ngp9= flux_radio_ngp9*1.0e6
error_radio_ngp9= error_radio_ngp9*1.0e6

flux_radio_g018= flux_radio_g018*1.0e6
error_radio_g018= error_radio_g018*1.0e6

#------------------------excluding flux < 25 mJy at 350 micron--------------------------------------------

flux_350_all=[]
error_350_all=[]
flux_radio_all=[]
error_radio_all=[]

flux_350_atca=[]
error_350_atca=[]
flux_radio_atca=[]
error_radio_atca=[]

for i in range(0,len(flux_350_bootes1)):
    if flux_350_bootes1[i] >= 20.0:  #=============================================HERE: flux limit=25 mJy
        flux_350_all.append(flux_350_bootes1[i])
        error_350_all.append(error_350_bootes1[i])
        flux_radio_all.append(flux_radio_bootes1[i])
        error_radio_all.append(error_radio_bootes1[i])



for i in range(0,len(flux_350_g12)):
    if flux_350_g12[i] >= 20.0:  #=============================================HERE: flux limit=25 mJy
        flux_350_all.append(flux_350_g12[i])
        error_350_all.append(error_350_g12[i])
        flux_radio_all.append(flux_radio_g12[i])
        error_radio_all.append(error_radio_g12[i])   

for i in range(0,len(flux_350_lockman)):
    if flux_350_lockman[i] >= 20.0:  #=============================================HERE: flux limit=25 mJy
        flux_350_all.append(flux_350_lockman[i])
        error_350_all.append(error_350_lockman[i])
        flux_radio_all.append(flux_radio_lockman[i])
        error_radio_all.append(error_radio_lockman[i])             


for i in range(0,len(flux_350_ngp1)):
    if flux_350_ngp1[i] >= 20.0:  #=============================================HERE: flux limit=25 mJy
        flux_350_all.append(flux_350_ngp1[i])
        error_350_all.append(error_350_ngp1[i])
        flux_radio_all.append(flux_radio_ngp1[i])
        error_radio_all.append(error_radio_ngp1[i])  


for i in range(0,len(flux_350_ngp3)):
    if flux_350_ngp3[i] >= 20.0:  #=============================================HERE: flux limit=25 mJy
        flux_350_all.append(flux_350_ngp3[i])
        error_350_all.append(error_350_ngp3[i])
        flux_radio_all.append(flux_radio_ngp3[i])
        error_radio_all.append(error_radio_ngp3[i])               


for i in range(0,len(flux_350_ngp5)):
    if flux_350_ngp5[i] >= 20.0:  #=============================================HERE: flux limit=25 mJy
        flux_350_all.append(flux_350_ngp5[i])
        error_350_all.append(error_350_ngp5[i])
        flux_radio_all.append(flux_radio_ngp5[i])
        error_radio_all.append(error_radio_ngp5[i])             



for i in range(0,len(flux_350_ngp6)):
    if flux_350_ngp6[i] >= 20.0:  #=============================================HERE: flux limit=25 mJy
        flux_350_all.append(flux_350_ngp6[i])
        error_350_all.append(error_350_ngp6[i])
        flux_radio_all.append(flux_radio_ngp6[i])
        error_radio_all.append(error_radio_ngp6[i])            


for i in range(0,len(flux_350_ngp7)):
    if flux_350_ngp7[i] >= 20.0:  #=============================================HERE: flux limit=25 mJy
        flux_350_all.append(flux_350_ngp7[i])
        error_350_all.append(error_350_ngp7[i])
        flux_radio_all.append(flux_radio_ngp7[i])
        error_radio_all.append(error_radio_ngp7[i])   


for i in range(0,len(flux_350_ngp9)):
    if flux_350_ngp9[i] >= 20.0:  #=============================================HERE: flux limit=25 mJy
        flux_350_all.append(flux_350_ngp9[i])
        error_350_all.append(error_350_ngp9[i])
        flux_radio_all.append(flux_radio_ngp9[i])
        error_radio_all.append(error_radio_ngp9[i])         


for i in range(0,len(flux_350_g018)):
    if flux_350_g018[i] >= 20.0:  #=============================================HERE: flux limit=25 mJy
        flux_350_atca.append(flux_350_g018[i])
        error_350_atca.append(error_350_g018[i])
        flux_radio_atca.append(flux_radio_g018[i])
        error_radio_atca.append(error_radio_g018[i])         


print flux_350_all
print error_350_all
print flux_350_atca
print error_350_atca
print 'ggggggggggggggggggggggggggggggggggg'

#===================================================Put FIR-radio correlation model in=============================

flux_6gz_model=np.arange(1.0e-5, 5.0e-4, 5.0e-7)  #========================================================HERE: 10-100 uJy (unit in Jy)

#print flux_6gz


flux_350_model=[]  #in Jy

for i in range(0,len(flux_6gz_model)):

    #flux_350_model.append(1.167e-12*pow(10.0,2.5)*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])  #1.167e-12: 1/350micron in 1/Hz. Approximate FIR flux~350 flux
    flux_350_model.append(1.167e-12*pow(10.0,2.0)*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])   #assume q_IR=2.0, radio spec index=0.8 ================================HERE

#print flux_350

flux_6gz_model = np.array(flux_6gz_model)
flux_6gz_model=np.array([float(i) for i in flux_6gz_model])
flux_350_model = np.array(flux_350_model)
flux_350_model=np.array([float(i) for i in flux_350_model])

flux_6gz_ujy_model=flux_6gz_model*1.0e6
flux_350_mjy_model=flux_350_model*1000.0







#==============================================Plotting===========================================================

#print flux_radio_bootes1
#print error_radio_bootes1

#plt.scatter(flux_350_bootes1, flux_radio_bootes1, color='blue', s=100.0)
#plt.errorbar(flux_350_bootes1, flux_radio_bootes1, xerr=error_350_bootes1, yerr=error_radio_bootes1, color='b',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)

#plt.scatter(flux_350_g12, flux_radio_g12, color='blue', s=100.0)
#plt.errorbar(flux_350_g12, flux_radio_g12, xerr=error_350_g12, yerr=error_radio_g12, color='b',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)

#plt.scatter(flux_350_lockman, flux_radio_lockman, color='blue', s=100.0)
#plt.errorbar(flux_350_lockman, flux_radio_lockman, xerr=error_350_lockman, yerr=error_radio_lockman, color='b',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)

#plt.scatter(flux_350_ngp1, flux_radio_ngp1, color='blue', s=100.0)
#plt.errorbar(flux_350_ngp1, flux_radio_ngp1, xerr=error_350_ngp1, yerr=error_radio_ngp1, color='b',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)

#plt.scatter(flux_350_ngp3, flux_radio_ngp3, color='blue', s=100.0)
#plt.errorbar(flux_350_ngp3, flux_radio_ngp3, xerr=error_350_ngp3, yerr=error_radio_ngp3, color='b',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)

#plt.scatter(flux_350_ngp5, flux_radio_ngp5, color='blue', s=100.0)
#plt.errorbar(flux_350_ngp5, flux_radio_ngp5, xerr=error_350_ngp5, yerr=error_radio_ngp5, color='b',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)

#plt.scatter(flux_350_ngp6, flux_radio_ngp6, color='blue', s=100.0)
#plt.errorbar(flux_350_ngp6, flux_radio_ngp6, xerr=error_350_ngp6, yerr=error_radio_ngp6, color='b',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)

#plt.scatter(flux_350_ngp7, flux_radio_ngp7, color='blue', s=100.0)
#plt.errorbar(flux_350_ngp7, flux_radio_ngp7, xerr=error_350_ngp7, yerr=error_radio_ngp7, color='b',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)

#plt.scatter(flux_350_ngp9, flux_radio_ngp9, color='blue', s=100.0)
#plt.errorbar(flux_350_ngp9, flux_radio_ngp9, xerr=error_350_ngp9, yerr=error_radio_ngp9, color='b',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)

plt.scatter(flux_350_all, flux_radio_all, color='blue', s=100.0, label='VLA')
plt.errorbar(flux_350_all, flux_radio_all, xerr=error_350_all, yerr=error_radio_all, color='b',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)

plt.scatter(flux_350_atca, flux_radio_atca, color='y', s=100.0, label='ATCA')
plt.errorbar(flux_350_atca, flux_radio_atca, xerr=error_350_atca, yerr=error_radio_atca, color='y',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)

plt.plot(flux_350_mjy_model, flux_6gz_ujy_model, color='red', linewidth=2.0, label='q_IR=2.0, alpha=0.8')

plt.legend(loc=1)
plt.xscale('log', nonposx='clip')
plt.yscale('log', nonposy='clip')

#plt.xlimit([0.0,1000.0])
#plt.ylimit([])
plt.plot(10.0,17.0, marker='+',markeredgewidth=3, color='m')

plt.grid()
plt.xlabel('F350 (mJy)')  #==========================================================HERE
plt.ylabel('6 GHz flux (uJy)')  #==========================================================HERE
plt.rc('font', size=30)
plt.show()


