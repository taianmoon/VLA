import matplotlib.pyplot as plt
import numpy as np
import math
#import matplotlib.cm as cm
#from astropy.io import fits
#import astropy.wcs as wcs
#from scipy.interpolate import interp1d


cluster_list=['bootes1', 'H12-00', 'Lockman1', 'NGP1', 'NGP3', 'NGP5', 'NGP6', 'NGP7', 'NGP9']
#cluster_list=['bootes1']

Nc_Nexp_literature=[0.0,0.0,0.0,0.0,0.0,0.85,0.91,1.35,1.25,1.46,1.6,4.96,5.25,7.2,14.45,11.11]  #1.0e-2
Nc_Nexp_literature_err=[0.0,0.0,0.0,0.0,0.0,0.2,0.25,0.25,0.29,0.33,0.51,1.28,2.07,3.47,7.01,7.58]  #1.0e-2
S_avg=[8.5,12.0,17.0,24.0,34.0,49.0,68.0,96.0,135.0,206.0,368.0,589.0,1084.0,1802.0,2960.0,4367.0]  #micro-Jy

S_avg_ngp9=[8.5,12.0,17.0,24.0,34.0]
ncounts_ngp9=np.array([0.0,0.0,0.0819844343536605,0.14561243648988484,0.3478304968993001])
#ncounts_err_ngp9=[0.0,0.0,0.057971749483216685,0.10296354126709305,0.2008200310171722]
completeness_err_ngp9 = np.array([1.000000000000000000e+00, 1.000000000000000000e+00, 1.000000000000000000e+00, 1.000000000000000000e+00, 2.539743835641491976e-02])
ncounts_err_ngp9 = ncounts_ngp9*completeness_err_ngp9  #propagated from completeness err (ncounts_ngp9*completeness_err)


fig, ax_all =plt.subplots(3,3, figsize=(16.0, 10.0), sharex=True, sharey=True)

#S_avg_rebin=[10.25, 20.5, 41.5, 82.0, 170.5, 478.5, 1443.0, 3663.5]

for l in range(0, len(cluster_list)):


    print cluster_list[l]


    template_file = open("./190802/ncounts_"+cluster_list[l]+".cat", "r")    #==================================================================================================HERE


    #lines = template_file.readlines()[1:]
    lines = template_file.readlines()
    template_file.close()

    response_curve=[]

    for i in range(0, len(lines)):
        separated_lines=lines[i].split() 
        response_curve.append(separated_lines)


    response_curve = np.array(response_curve)
    ncounts=response_curve[:,0]      #=========================================================HERE: 7 for Todd's cluster, 6 for our clusters
    ncounts_err=response_curve[:,1]    #=========================================================HERE: 8 for Todd's cluster, 7 for our clusters



    ncounts = np.array(ncounts)
    ncounts_err = np.array(ncounts_err)
    ncounts=np.array([float(i) for i in ncounts])  #(wavelength in angstrom)
    ncounts_err=np.array([float(i) for i in ncounts_err])  #(wavelength in angstrom)



    #-------------------Load in completeness errors------------------------
    template_file = open("../completeness/output/"+cluster_list[l]+"_completeness_level_origflux.cat", "r")   

    lines = template_file.readlines()[1:]
    #lines = template_file.readlines()
    template_file.close()

    response_curve=[]

    for i in range(0, len(lines)):
        separated_lines=lines[i].split() 
        response_curve.append(separated_lines)


    response_curve = np.array(response_curve)
    completeness = response_curve[:,1]      #=========================================================HERE: 7 for Todd's cluster, 6 for our clusters
    completeness_err = response_curve[:,2]    #=========================================================HERE: 8 for Todd's cluster, 7 for our clusters


    completeness = np.array(completeness)
    completeness = np.array([float(i) for i in completeness])  #(wavelength in angstrom)
    completeness_err = np.array(completeness_err)
    completeness_err = np.array([float(i) for i in completeness_err])  #(wavelength in angstrom)


    #Nc_Nexp_us_err_completeness = (Nc_Nexp_us/completeness)*completeness_err
    #Nc_Nexp_us_err_completeness = (ncounts_rebin/1.0)*completeness_err

    #----------------------------------------------------------------------



    #----------------------rebin: combine two tgt-----------------------------------
    completeness_rebin=[]
    completeness_err_rebin=[]
    ncounts_rebin=[]
    ncounts_err_rebin=[]
    S_avg_rebin=[]
    for rb in range(0, len(S_avg)):
        if rb%2 == 0: #even
            if ncounts[rb]==0.0: 
                S_avg_rebin.append(S_avg[rb+1])
                ncounts_rebin.append(ncounts[rb+1])
                ncounts_err_rebin.append(ncounts_err[rb+1])
                completeness_rebin.append(completeness[rb+1])
                completeness_err_rebin.append(completeness_err[rb+1])
            elif ncounts[rb+1]==0.0:
                S_avg_rebin.append(S_avg[rb])
                ncounts_rebin.append(ncounts[rb])
                ncounts_err_rebin.append(ncounts_err[rb])
                completeness_rebin.append(completeness[rb])
                completeness_err_rebin.append(completeness_err[rb])
            else:
                S_avg_rebin.append((S_avg[rb]+S_avg[rb+1])/2.0)
                ncounts_rebin.append((ncounts[rb]+ncounts[rb+1])/2.0)
                ncounts_err_rebin.append(math.sqrt(pow(ncounts_err[rb], 2)+pow(ncounts_err[rb+1], 2))/2.0)
                completeness_rebin.append((completeness[rb]+completeness[rb+1])/2.0)
                completeness_err_rebin.append(math.sqrt(pow(completeness_err[rb], 2)+pow(completeness_err[rb+1], 2))/2.0)

    print ncounts_rebin
    print ncounts_err_rebin
    ncounts_rebin = np.array(ncounts_rebin)
    ncounts_rebin = np.array([float(i) for i in ncounts_rebin])  #(wavelength in angstrom)
    completeness_rebin = np.array(completeness_rebin)
    completeness_rebin = np.array([float(i) for i in completeness_rebin])  #(wavelength in angstrom)
    completeness_err_rebin = np.array(completeness_err_rebin)
    completeness_err_rebin = np.array([float(i) for i in completeness_err_rebin])  #(wavelength in angstrom)
    print 'ffffffffffffffffffffffff'

    Nc_Nexp_us_err_completeness = (ncounts_rebin/1.0)*completeness_err_rebin


    #==========================Plotting=============================================================================
    if 0<=l<=2:
        ax=ax_all[0,l]
    elif 3<=l<=5:
        ax=ax_all[1,l-3]
    else:
        ax=ax_all[2,l-6]







    ax.scatter(S_avg, Nc_Nexp_literature, color='r', s=40, label='Huynh et al. (2015)')
    ax.errorbar(S_avg, Nc_Nexp_literature, yerr=Nc_Nexp_literature_err, color='r', fmt='o', elinewidth=2.0, capsize=5.0, capthick=2.0, markeredgewidth=2) 

    #ax.scatter(S_avg, ncounts, color='b', s=40, marker='s', label='This work') 
    #ax.errorbar(S_avg, ncounts, yerr=ncounts_err, color='b', fmt='o', elinewidth=2.0, capsize=5.0, capthick=2.0, markeredgewidth=2) 
    ax.scatter(S_avg_rebin, ncounts_rebin, color='b', s=40, marker='s', label='This work') 
    #ax.errorbar(S_avg_rebin, ncounts_rebin, yerr=ncounts_err_rebin, color='b', fmt='o', elinewidth=2.0, capsize=5.0, capthick=2.0, markeredgewidth=2) 
    ax.errorbar(S_avg_rebin, ncounts_rebin, yerr=Nc_Nexp_us_err_completeness, color='b', fmt='o', elinewidth=2.0, capsize=5.0, capthick=2.0, markeredgewidth=2) 





    ax.scatter(S_avg_ngp9, ncounts_ngp9, color='gray', s=40, marker='s') 
    ax.errorbar(S_avg_ngp9, ncounts_ngp9, yerr=ncounts_err_ngp9, color='gray', fmt='o', elinewidth=2.0, capsize=5.0, capthick=2.0, markeredgewidth=2) 

    ax.tick_params(width=2, length=16, which='major')
    ax.tick_params(width=2, length=5, which='minor')

    ax.set_xlim((10.0, 1e4))
    ax.set_ylim((1e-2, 1e2))

    #leg = ax.legend(handlelength=0, handletextpad=0, fancybox=True, loc='upper right')
    ##print leg
    ##print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    #for item in leg.legendHandles:
    #    item.set_visible(False)
    #leg.get_frame().set_linewidth(0.0)
    #leg.get_frame().set_alpha(0.75)


    if 6<=l<=8:
        ax.set_xlabel(r'$S(6cm)$ [$\mu$Jy]')  
    #ax.title(cluster_list[l])  #===============================================================================================================HERE
    if l==0 or l==3 or l==6:
        ax.set_ylabel(r'$N_c/N_{exp}$ [1x$10^{-2}$]')  

    ax.text(16.7, 27.0, cluster_list[l], fontsize=20)


    ax.grid()
    ax.set_xscale('log',nonposy='clip')
    ax.set_yscale('log',nonposy='clip')
    #ax.set_xlabel(r'$S(6cm)$ [$\mu$Jy]')
    #ax.set_ylabel(r'$N_c/N_{exp}$ [1x$10^{-2}$]')

    #plt.legend(loc=2)
    #plt.title(cluster_list[l])   #======================================================================================================================================HERE

    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc=(0.75, 0.1))

plt.rc('font', size=20) 
plt.show()



