import pyfits
import matplotlib.pyplot as plt
import numpy as np
import math
import glob
import os.path




names_wht = pyfits.open('../'+cluster_list[l]+'_VLA_Herschel_match.fits')                            #========================================================HERE
names_wht_data = names_wht[1].data
names_wht.close()

#flux_250= names_wht_data.field('F250')    #========================================================HERE(Bootes: F250, et_F250; EGS/NGP9: f250, et250; G12/NGP: F250, E250)
#error_250= names_wht_data.field('et_f250')    #========================================================HER
flux_350= names_wht_data.field('F350')    #========================================================HER


if cluster_list[l]=='Bootes1':
    error_350 = names_wht_data.field('et_F350')    #========================================================HER
else:
    error_350 = names_wht_data.field('E350')    #========================================================HER

#error_350= names_wht_data.field('et_f350')    #========================================================HER
#flux_500= names_wht_data.field('F500')    #========================================================HER
#error_500= names_wht_data.field('et_f500')    #========================================================HER
flux_radio= names_wht_data.field('col38')
error_radio= names_wht_data.field('col39')



#flux_250 = np.array(flux_250)
#flux_250=np.array([float(i) for i in flux_250])
#error_250 = np.array(error_250)
#error_250=np.array([float(i) for i in error_250])
flux_350 = np.array(flux_350)
flux_350=np.array([float(i) for i in flux_350])
error_350 = np.array(error_350)
error_350=np.array([float(i) for i in error_350])
#flux_500 = np.array(flux_500)
#flux_500=np.array([float(i) for i in flux_500])
#error_500 = np.array(error_500)
#error_500=np.array([float(i) for i in error_500])
flux_radio = np.array(flux_radio)
flux_radio=np.array([float(i) for i in flux_radio])
error_radio = np.array(error_radio)
error_radio=np.array([float(i) for i in error_radio])

#print error_radio_bootes1





if cluster_list[l] == 'G12' or cluster_list[l] == 'NGP1' or cluster_list[l] == 'NGP3' or cluster_list[l] == 'NGP5' or cluster_list[l] == 'NGP6' or cluster_list[l] == 'NGP7' or cluster_list[l] == 'NGP9' or cluster_list[l] == 'G018':

    flux_350=flux_350*1000.0
    error_350=error_350*1000.0



#---------------------------------------------------------------------

flux_radio= flux_radio*1.0e6
error_radio= error_radio*1.0e6


#------------------------excluding flux < 25 mJy at 350 micron--------------------------------------------

flux_350_all=[]
error_350_all=[]
flux_radio_all=[]
error_radio_all=[]



for i in range(0,len(flux_350)):
    if flux_350[i] >= 20.0:  #=============================================HERE: flux limit=25 mJy
        flux_350_all.append(flux_350[i])
        error_350_all.append(error_350[i])
        flux_radio_all.append(flux_radio[i])
        error_radio_all.append(error_radio[i])


print flux_350_all
print error_350_all
print 'ggggggggggggggggggggggggggggggggggg'

#===================================================Put FIR-radio correlation model in=============================

flux_6gz_model=np.arange(1.0e-5, 5.0e-3, 5.0e-7)  #========================================================HERE: 10-1000 uJy (unit in Jy)

#print flux_6gz


flux_350_model_z0=[]  #in Jy
flux_350_model_z1=[]  #in Jy
flux_350_model_z2=[]  #in Jy
flux_350_model_z3=[]  #in Jy
flux_350_model_z4=[]  #in Jy

for i in range(0,len(flux_6gz_model)):

    #flux_350_model.append(1.167e-12*pow(10.0,2.5)*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])
    #flux_350_model.append(1.167e-12*pow(10.0,2.0)*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])   #assume q_IR=2.0, radio spec index=0.8 ================================HERE: why 1.167e-12??
    flux_350_model_z0.append(1.167e-12*pow(10.0,2.35)*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])  #q(z) following eq.6 of Magnelli 2015
    flux_350_model_z1.append(1.167e-12*pow(10.0,2.35*pow(2, -0.12))*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])  #q(z) following eq.6 of Magnelli 2015
    flux_350_model_z2.append(1.167e-12*pow(10.0,2.35*pow(3, -0.12))*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])  #q(z) following eq.6 of Magnelli 2015
    flux_350_model_z3.append(1.167e-12*pow(10.0,2.35*pow(4, -0.12))*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])  #q(z) following eq.6 of Magnelli 2015
    flux_350_model_z4.append(1.167e-12*pow(10.0,2.35*pow(5, -0.12))*3.75e12*pow(6.0/1.4,0.8)*flux_6gz_model[i])  #q(z) following eq.6 of Magnelli 2015

#print flux_350

flux_6gz_model = np.array(flux_6gz_model)
flux_6gz_model=np.array([float(i) for i in flux_6gz_model])
flux_350_model_z0 = np.array(flux_350_model_z0)
flux_350_model_z0=np.array([float(i) for i in flux_350_model_z0])
flux_350_model_z1 = np.array(flux_350_model_z1)
flux_350_model_z1=np.array([float(i) for i in flux_350_model_z1])
flux_350_model_z2 = np.array(flux_350_model_z2)
flux_350_model_z2=np.array([float(i) for i in flux_350_model_z2])
flux_350_model_z3 = np.array(flux_350_model_z3)
flux_350_model_z3=np.array([float(i) for i in flux_350_model_z3])
flux_350_model_z4 = np.array(flux_350_model_z4)
flux_350_model_z4=np.array([float(i) for i in flux_350_model_z4])

flux_6gz_ujy_model=flux_6gz_model*1.0e6
flux_350_mjy_model_z0=flux_350_model_z0*1000.0
flux_350_mjy_model_z1=flux_350_model_z1*1000.0
flux_350_mjy_model_z2=flux_350_model_z2*1000.0
flux_350_mjy_model_z3=flux_350_model_z3*1000.0
flux_350_mjy_model_z4=flux_350_model_z4*1000.0







#=============================================Fit a straight line to the data=====================================


#---------excluding possible AGNs-------

flux_350_all_noagn=[]
flux_radio_all_noagn=[]
error_350_all_noagn=[]
error_radio_all_noagn=[]


for i in range(0,len(flux_350_all)):
    #if 0.85*np.log10(flux_350_all[i]) + 0.6 >= np.log10(flux_radio_all[i]):  #=============================================HERE: slope and intersection of excluding AGN line
    if 0.85*np.log10(flux_350_all[i]) + 0.5 >= np.log10(flux_radio_all[i]):  #=============================================HERE: slope and intersection of excluding AGN line
    
        flux_350_all_noagn.append(flux_350_all[i])
        flux_radio_all_noagn.append(flux_radio_all[i])
        error_350_all_noagn.append(error_350_all[i])
        error_radio_all_noagn.append(error_radio_all[i])



#--------------------------------------------


flux_350_all_log=np.log10(flux_350_all_noagn)
flux_radio_all_log=np.log10(flux_radio_all_noagn)



z = np.polyfit(flux_350_all_log, flux_radio_all_log, 1)
#z = np.polyfit(flux_350_all, flux_radio_all, 1)


#print 'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH'

#print z
#print z[0]
#print z[1]

straight_line_x=np.arange(1.0,3.0,0.01)

#straight_line_x=np.logspace(0.0, 3.0, num=100)
straight_line_y=[]
straight_line_y_toy=[]

for i in range(0,len(straight_line_x)):

    straight_line_y.append(z[0]*straight_line_x[i]+z[1])
    #straight_line_y_atca.append(z_atca[0]*straight_line_x_atca[i]+z_atca[1])
    straight_line_y_toy.append(0.85*straight_line_x[i]+0.6)    #=============================================HERE: slope and intersection of excluding AGN line

straight_line_x = np.array(straight_line_x)
straight_line_x=np.array([float(i) for i in straight_line_x])
straight_line_y = np.array(straight_line_y)
straight_line_y=np.array([float(i) for i in straight_line_y])
#straight_line_x_atca = np.array(straight_line_x_atca)
#straight_line_x_atca=np.array([float(i) for i in straight_line_x_atca])
#straight_line_y_atca = np.array(straight_line_y_atca)
#straight_line_y_atca=np.array([float(i) for i in straight_line_y_atca])
straight_line_y_toy = np.array(straight_line_y_toy)
straight_line_y_toy=np.array([float(i) for i in straight_line_y_toy])

straight_line_x_log=pow(10.0,straight_line_x)
straight_line_y_log=pow(10.0,straight_line_y)
#straight_line_x_log_atca=pow(10.0,straight_line_x_atca)
#straight_line_y_log_atca=pow(10.0,straight_line_y_atca)
straight_line_y_log_toy=pow(10.0,straight_line_y_toy)

print straight_line_x
print straight_line_y
#print straight_line_x_atca
#print straight_line_y_atca

#plt.plot(straight_line_x_log, straight_line_y_log, color='blue', linewidth=2.0)
#plt.plot(straight_line_x_log_atca, straight_line_y_log_atca, color='y', linewidth=2.0)
#plt.plot(straight_line_x_log, straight_line_y_log_toy, ':')






#==============================================Plotting===========================================================

if 0<=l<=1:
    ax=ax_all[0,l]
elif 2<=l<=3:
    ax=ax_all[1,l-2]
elif 4<=l<=5:
    ax=ax_all[2,l-4]
elif 6<=l<=7:
    ax=ax_all[3,l-6]
else:
    ax=ax_all[4,l-8]


ax.plot(straight_line_x_log, straight_line_y_log, color='blue', linewidth=2.0)

ax.scatter(flux_350_all_noagn, flux_radio_all_noagn, color='blue', s=100.0)
ax.errorbar(flux_350_all_noagn, flux_radio_all_noagn, xerr=error_350_all_noagn, yerr=error_radio_all_noagn, color='b',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)


ax.plot(flux_350_mjy_model_z0, flux_6gz_ujy_model, ':', color='red', linewidth=2.0)
ax.plot(flux_350_mjy_model_z1, flux_6gz_ujy_model, ':', color='red', linewidth=2.0)
ax.plot(flux_350_mjy_model_z2, flux_6gz_ujy_model, ':', color='red', linewidth=2.0)
ax.plot(flux_350_mjy_model_z3, flux_6gz_ujy_model, ':', color='red', linewidth=2.0)
ax.plot(flux_350_mjy_model_z4, flux_6gz_ujy_model, ':', color='red', linewidth=2.0)

ax.text(flux_350_mjy_model_z0[200],flux_6gz_ujy_model[200], 'z=0', color='red', fontsize=20.0)
ax.text(flux_350_mjy_model_z4[300],flux_6gz_ujy_model[300], 'z=4', color='red', fontsize=20.0)

#plt.legend(loc=1)
ax.set_xscale('log', nonposx='clip')
ax.set_yscale('log', nonposy='clip')

ax.set_xlim([10.0,1000.0])
ax.set_ylim([10.0, 1000.0])
#plt.plot(10.0,17.0, marker='+',markeredgewidth=3, color='m')


if 8<=l<=9:
    ax.set_xlabel('F350 (mJy)')  
#ax.title(cluster_list[l])  #===============================================================================================================HERE
if l==0 or l==2 or l==4 or l==6 or l==8:
    ax.set_ylabel(r'6 GHz flux ($\mu$Jy)')  

ax.text(12.0, 500.0, cluster_list[l], fontsize=20)

ax.grid()
#ax.set_xlabel('F350 (mJy)')  #==========================================================HERE
#ax.set_ylabel('6 GHz flux (uJy)')  #==========================================================HERE
#plt.rc('font', size=30)
#plt.show()


