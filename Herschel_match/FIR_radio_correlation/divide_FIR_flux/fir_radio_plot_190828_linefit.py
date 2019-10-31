import pyfits
import matplotlib.pyplot as plt
import numpy as np
import math
import glob
import os.path


#=========================Import Berta's template=====================================

sed_data = open('../templates_berta/Red_SF_glx_2.norm_LIR', 'r')

#figure_title = os.path.splitext(filename)[0]

x=[]
y=[]
z=[]

for line in sed_data:
    columns = line.split()
    x.append(columns[0])
    y.append(columns[1])
    
x = np.array(x)
y = np.array(y)

x=np.array([float(i) for i in x])
y=np.array([float(i) for i in y])

z=x*x*y*1.0e12*1.0e-10/3.0e8
z=z*3.846e52  #change from L_solar/m^2Hz flux to Jy
x=x*1.0e-10*1.0e6 #change from angstrom to micron

sed_data.close()


print z
print x


#plt.plot(x, z)
#plt.xscale('log', nonposx='clip')
#plt.yscale('log', nonposy='clip')

#plt.show()





#mock_catalogue=np.array((1000*np.logspace(-2, 0, num=100)))

#---------redshift x--------------------------
redshift_grid=[1.0, 1.25, 1.5, 1.75, 2.0, 2.25]

for j in range(0, len(redshift_grid)):    #=================================================loop over different redshifts

    x_loop=x*(1+redshift_grid[j])



    #============================Given 350 micron flux, normalise Berta's template to get 60 and 100 mircon flux=========================


    flux_350_model=np.logspace(-2, 0, num=100)  #========================================================HERE: 10-1000 mJy (unit in Jy)
    #flux_350_model=0.03




    #print np.interp(350.0, x_loop, z)


    flux_6GHz_overall=[]
    for i in range(0, len(flux_350_model)):  #=============================================Loop over different F350 values

        z_inloop=z*(flux_350_model[i]/np.interp(350.0, x_loop, z))


        #print z_inloop

        #plt.plot(x_loop, z)
        #plt.xscale('log', nonposx='clip')
        #plt.yscale('log', nonposy='clip')
        #plt.tick_params(width=2, length=16, which='major')
        #plt.tick_params(width=2, length=5, which='minor')

        #plt.show()


        flux_60_model = np.interp(60.0, x_loop, z_inloop)  #Jy
        flux_100_model = np.interp(100.0, x_loop, z_inloop)  #Jy


        #print flux_60_model
        #print flux_100_model

        FIR = 1.26e-14*(2.58*flux_60_model + flux_100_model)  #W/m^2

        #print FIR
        #print 'fffffffffffffffffffff'

        flux_1p4GHz = 1e26*FIR/(3.75e12*1e2)  #[W/m^2/Hz] to Jy, 1e2: assuming q=2
        flux_6GHz = pow(1.4/6, 0.8)*flux_1p4GHz  #Jy


        #print flux_6GHz

        flux_6GHz_overall.append(flux_6GHz)


    print flux_6GHz_overall

    #mock_catalogue=np.c_((mock_catalogue, np.array(flux_6GHz_overall)*1e6))

    flux_350_model=np.array(flux_350_model)*1000       #mJy
    flux_6GHz_overall=np.array(flux_6GHz_overall)*1e6  #uJy
    plt.plot(flux_350_model, flux_6GHz_overall, ':', color='black', linewidth=2.0)
    plt.text(flux_350_model[-40], flux_6GHz_overall[-40], 'z='+str(redshift_grid[j]), color='black', fontsize=20.0)

#plt.xscale('log', nonposx='clip')
#plt.yscale('log', nonposy='clip')
#plt.tick_params(width=2, length=16, which='major')
#plt.tick_params(width=2, length=5, which='minor')
#plt.xlabel('F350 (mJy)')
#plt.ylabel('F6GHz (uJy)')
#plt.xlim([10, 1000])
#plt.ylim([10, 1000])
#plt.rc('font', size=15)
#plt.grid()
#plt.show()






#=========================================================Start to input data====================================================================================



#----------------Bootes1

names_wht_bootes1 = pyfits.open('./Bootes1_VLA_Herschel_match.fits')                            #========================================================HERE
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

names_wht_g12 = pyfits.open('./G12_VLA_Herschel_match.fits')                            #========================================================HERE
#names_wht_g12 = pyfits.open('../G12_VLA_Herschel_match_nolens.fits')                            #========================================================HERE
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

names_wht_lockman = pyfits.open('./Lockman_VLA_Herschel_match.fits')                            #========================================================HERE
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

names_wht_ngp1 = pyfits.open('./NGP1_VLA_Herschel_match.fits')                            #========================================================HERE
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

names_wht_ngp3 = pyfits.open('./NGP3_VLA_Herschel_match.fits')                            #========================================================HERE
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

names_wht_ngp5 = pyfits.open('./NGP5_VLA_Herschel_match.fits')                            #========================================================HERE
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

names_wht_ngp6 = pyfits.open('./NGP6_VLA_Herschel_match.fits')                            #========================================================HERE
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

names_wht_ngp7 = pyfits.open('./NGP7_VLA_Herschel_match.fits')                            #========================================================HERE
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

names_wht_ngp9 = pyfits.open('./NGP9_VLA_Herschel_match.fits')                            #========================================================HERE
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

names_wht_g018 = pyfits.open('./G018_VLA_Herschel_match.fits')                            #========================================================HERE
names_wht_data = names_wht_g018[1].data
names_wht_g018.close()


flux_350_g018= names_wht_data.field('F350')    #========================================================HER
error_350_g018= names_wht_data.field('e350')    #========================================================HER
flux_radio_g018_pre= names_wht_data.field('col38')
error_radio_g018= names_wht_data.field('col39')

flux_350_g018 = np.array(flux_350_g018)
flux_350_g018=np.array([float(i) for i in flux_350_g018])
error_350_g018 = np.array(error_350_g018)
error_350_g018=np.array([float(i) for i in error_350_g018])
flux_radio_g018_pre = np.array(flux_radio_g018_pre)
flux_radio_g018_pre=np.array([float(i) for i in flux_radio_g018_pre])
error_radio_g018 = np.array(error_radio_g018)
error_radio_g018=np.array([float(i) for i in error_radio_g018])

flux_350_g018=flux_350_g018*1000.0
error_350_g018=error_350_g018*1000.0


flux_radio_g018 = flux_radio_g018_pre*pow(5.5/6.0, 0.8)  #convert ATCA flux from 5.5 to 6 GHz, to match VLA

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

##===================================================Put FIR-radio correlation model in=============================
#
#flux_6gz_model=np.arange(1.0e-5, 5.0e-3, 5.0e-7)  #========================================================HERE: 10-1000 uJy (unit in Jy)
#
##print flux_6gz
#
#
#flux_350_model_z0=[]  #in Jy
#flux_350_model_z1=[]  #in Jy
#flux_350_model_z2=[]  #in Jy
#flux_350_model_z3=[]  #in Jy
#flux_350_model_z4=[]  #in Jy
#
#for i in range(0,len(flux_6gz_model)):
#
#    #flux_350_model.append(1.167e-12*pow(10.0,2.5)*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])
#    #flux_350_model.append(1.167e-12*pow(10.0,2.0)*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])   #assume q_IR=2.0, radio spec index=0.8 ================================HERE: why 1.167e-12??
#    flux_350_model_z0.append(1.167e-12*pow(10.0,2.35)*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])  #q(z) following eq.6 of Magnelli 2015
#    flux_350_model_z1.append(1.167e-12*pow(10.0,2.35*pow(2, -0.12))*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])  #q(z) following eq.6 of Magnelli 2015
#    flux_350_model_z2.append(1.167e-12*pow(10.0,2.35*pow(3, -0.12))*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])  #q(z) following eq.6 of Magnelli 2015
#    flux_350_model_z3.append(1.167e-12*pow(10.0,2.35*pow(4, -0.12))*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])  #q(z) following eq.6 of Magnelli 2015
#    flux_350_model_z4.append(1.167e-12*pow(10.0,2.35*pow(5, -0.12))*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])  #q(z) following eq.6 of Magnelli 2015
#
##print flux_350
#
#flux_6gz_model = np.array(flux_6gz_model)
#flux_6gz_model=np.array([float(i) for i in flux_6gz_model])
#flux_350_model_z0 = np.array(flux_350_model_z0)
#flux_350_model_z0=np.array([float(i) for i in flux_350_model_z0])
#flux_350_model_z1 = np.array(flux_350_model_z1)
#flux_350_model_z1=np.array([float(i) for i in flux_350_model_z1])
#flux_350_model_z2 = np.array(flux_350_model_z2)
#flux_350_model_z2=np.array([float(i) for i in flux_350_model_z2])
#flux_350_model_z3 = np.array(flux_350_model_z3)
#flux_350_model_z3=np.array([float(i) for i in flux_350_model_z3])
#flux_350_model_z4 = np.array(flux_350_model_z4)
#flux_350_model_z4=np.array([float(i) for i in flux_350_model_z4])
#
#flux_6gz_ujy_model=flux_6gz_model*1.0e6
#flux_350_mjy_model_z0=flux_350_model_z0*1000.0
#flux_350_mjy_model_z1=flux_350_model_z1*1000.0
#flux_350_mjy_model_z2=flux_350_model_z2*1000.0
#flux_350_mjy_model_z3=flux_350_model_z3*1000.0
#flux_350_mjy_model_z4=flux_350_model_z4*1000.0
#
#
#
#
#


#=============================================Fit a straight line to the data=====================================


#---------excluding possible AGNs-------

flux_350_all_noagn=[]
flux_radio_all_noagn=[]
error_350_all_noagn=[]
error_radio_all_noagn=[]

flux_350_atca_noagn=[]
flux_radio_atca_noagn=[]
error_350_atca_noagn=[]
error_radio_atca_noagn=[]

for i in range(0,len(flux_350_all)):
    #if 0.85*np.log10(flux_350_all[i]) + 0.6 >= np.log10(flux_radio_all[i]):  #=============================================HERE: slope and intersection of excluding AGN line
    if 0.85*np.log10(flux_350_all[i]) + 0.5 >= np.log10(flux_radio_all[i]):  #=============================================HERE: slope and intersection of excluding AGN line
    
        flux_350_all_noagn.append(flux_350_all[i])
        flux_radio_all_noagn.append(flux_radio_all[i])
        error_350_all_noagn.append(error_350_all[i])
        error_radio_all_noagn.append(error_radio_all[i])

for i in range(0,len(flux_350_atca)):
    #if 0.85*np.log10(flux_350_atca[i]) + 0.6 >= np.log10(flux_radio_atca[i]):  #=============================================HERE: slope and intersection of excluding AGN line
    if 0.85*np.log10(flux_350_atca[i]) + 0.5 >= np.log10(flux_radio_atca[i]):  #=============================================HERE: slope and intersection of excluding AGN line
    
        flux_350_atca_noagn.append(flux_350_atca[i])
        flux_radio_atca_noagn.append(flux_radio_atca[i])
        error_350_atca_noagn.append(error_350_atca[i])
        error_radio_atca_noagn.append(error_radio_atca[i])


#--------------------------------------------


flux_350_all_log=np.log10(flux_350_all_noagn)
flux_radio_all_log=np.log10(flux_radio_all_noagn)
flux_350_atca_log=np.log10(flux_350_atca_noagn)
flux_radio_atca_log=np.log10(flux_radio_atca_noagn)


z = np.polyfit(flux_350_all_log, flux_radio_all_log, 1)
z_atca = np.polyfit(flux_350_atca_log, flux_radio_atca_log, 1)
#z = np.polyfit(flux_350_all, flux_radio_all, 1)


#print 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH'

#print z
#print z[0]
#print z[1]

straight_line_x=np.arange(1.0,3.0,0.01)
straight_line_x_atca=np.arange(1.0,3.0,0.01)
#straight_line_x=np.logspace(0.0, 3.0, num=100)
straight_line_y=[]
straight_line_y_atca=[]
straight_line_y_toy=[]

for i in range(0,len(straight_line_x)):

    straight_line_y.append(z[0]*straight_line_x[i]+z[1])
    straight_line_y_atca.append(z_atca[0]*straight_line_x_atca[i]+z_atca[1])
    #straight_line_y_toy.append(0.85*straight_line_x[i]+0.6)    #=============================================HERE: slope and intersection of excluding AGN line
    straight_line_y_toy.append(0.85*straight_line_x[i]+0.5)    #=============================================HERE: slope and intersection of excluding AGN line

straight_line_x = np.array(straight_line_x)
straight_line_x=np.array([float(i) for i in straight_line_x])
straight_line_y = np.array(straight_line_y)
straight_line_y=np.array([float(i) for i in straight_line_y])
straight_line_x_atca = np.array(straight_line_x_atca)
straight_line_x_atca=np.array([float(i) for i in straight_line_x_atca])
straight_line_y_atca = np.array(straight_line_y_atca)
straight_line_y_atca=np.array([float(i) for i in straight_line_y_atca])
straight_line_y_toy = np.array(straight_line_y_toy)
straight_line_y_toy=np.array([float(i) for i in straight_line_y_toy])

straight_line_x_log=pow(10.0,straight_line_x)
straight_line_y_log=pow(10.0,straight_line_y)
straight_line_x_log_atca=pow(10.0,straight_line_x_atca)
straight_line_y_log_atca=pow(10.0,straight_line_y_atca)
straight_line_y_log_toy=pow(10.0,straight_line_y_toy)

print straight_line_x
print straight_line_y
print straight_line_x_atca
print straight_line_y_atca

plt.plot(straight_line_x_log, straight_line_y_log, color='blue', linewidth=2.0)
plt.plot(straight_line_x_log_atca, straight_line_y_log_atca, color='red', linewidth=2.0)
#plt.plot(straight_line_x_log, straight_line_y_log_toy, ':')






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

plt.scatter(flux_350_all_noagn, flux_radio_all_noagn, color='blue', s=100.0, label='VLA')
plt.errorbar(flux_350_all_noagn, flux_radio_all_noagn, xerr=error_350_all_noagn, yerr=error_radio_all_noagn, color='b',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)

plt.scatter(flux_350_atca_noagn, flux_radio_atca_noagn, color='red', s=100.0, label='ATCA')
plt.errorbar(flux_350_atca_noagn, flux_radio_atca_noagn, xerr=error_350_atca_noagn, yerr=error_radio_atca_noagn, color='red',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)

#plt.plot(flux_350_mjy_model_z0, flux_6gz_ujy_model, ':', color='red', linewidth=2.0)
#plt.plot(flux_350_mjy_model_z1, flux_6gz_ujy_model, ':', color='red', linewidth=2.0)
#plt.plot(flux_350_mjy_model_z2, flux_6gz_ujy_model, ':', color='red', linewidth=2.0)
#plt.plot(flux_350_mjy_model_z3, flux_6gz_ujy_model, ':', color='red', linewidth=2.0)
#plt.plot(flux_350_mjy_model_z4, flux_6gz_ujy_model, ':', color='red', linewidth=2.0)

#plt.text(flux_350_mjy_model_z0[200],flux_6gz_ujy_model[200], 'z=0', color='red', fontsize=30.0)
#plt.text(flux_350_mjy_model_z4[300],flux_6gz_ujy_model[300], 'z=4', color='red', fontsize=30.0)

plt.legend(loc=1)
plt.xscale('log', nonposx='clip')
plt.yscale('log', nonposy='clip')

plt.tick_params(width=2, length=16, which='major')
plt.tick_params(width=2, length=5, which='minor')

plt.xlim([10, 1000])
plt.ylim([10, 1000])

#plt.xlimit([0.0,1000.0])
#plt.ylimit([])
#plt.plot(10.0,17.0, marker='+',markeredgewidth=3, color='m')

plt.grid()
plt.xlabel('F350 (mJy)')  #==========================================================HERE
plt.ylabel(r'6 GHz flux ($\mu$Jy)')  #==========================================================HERE
plt.rc('font', size=30)
plt.show()

