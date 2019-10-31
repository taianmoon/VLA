import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d



cluster_list=['bootes1', 'Lockman1', 'H12-00', 'NGP1', 'NGP3', 'NGP5', 'NGP6', 'NGP7', 'NGP9']
#cluster_list=['bootes1']  #==========================================================HERE


total_sources=15000  #==========================================================HERE




#wanted_flux=[2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]

wanted_flux=np.array([8.5,12.0,17.0,24.0,34.0,49.0,68.0,96.0,135.0,206.0,368.0,589.0,1084.0,1802.0,2960.0,4367.0])*0.001   #in mJy
figa, ax_all =plt.subplots(3,5, figsize=(16.0, 10.0), sharex=True, sharey=True)

for l in range(0, len(cluster_list)):

    
    print cluster_list[l]
    template_file = open("./output/"+cluster_list[l]+"_completeness_level.cat", "r") 

    lines = template_file.readlines()[1:]
    #lines = template_file.readlines()
    template_file.close()

    response_curve=[]

    for i in range(0, len(lines)):
        separated_lines=lines[i].split() 
        response_curve.append(separated_lines)


    response_curve = np.array(response_curve)

    flux_deboosted=response_curve[:,0]      #=========================================================HERE: 7 for Todd's cluster, 6 for our clusters
    completeness_level=response_curve[:,2]    #=========================================================HERE: 8 for Todd's cluster, 7 for our clusters

    flux_deboosted = np.array(flux_deboosted)
    completeness_level = np.array(completeness_level)
    flux_deboosted=np.array([float(i) for i in flux_deboosted])  #(wavelength in angstrom)
    completeness_level=np.array([float(i) for i in completeness_level])  #(wavelength in angstrom)


    print flux_deboosted
    print completeness_level


    fn_completelenss=interp1d(flux_deboosted, completeness_level, bounds_error=False, fill_value=(completeness_level[0], completeness_level[-1]))

    completeness_level_interpolate=[]
    completeness_level_interpolate_err=[]



    for wf in range(0, len(wanted_flux)):
        completeness_level_interpolate.append(fn_completelenss(wanted_flux[wf]))
        if fn_completelenss(wanted_flux[wf]) != 0.0:
            completeness_level_interpolate_err.append(pow(total_sources*fn_completelenss(wanted_flux[wf]), -0.5))
        else:
            completeness_level_interpolate_err.append(1.0)

    completeness_level_interpolate = np.array(completeness_level_interpolate)
    completeness_level_interpolate=np.array([float(i) for i in completeness_level_interpolate])  #(wavelength in angstrom)
    completeness_level_interpolate_err = np.array(completeness_level_interpolate_err)
    completeness_level_interpolate_err=np.array([float(i) for i in completeness_level_interpolate_err])  #(wavelength in angstrom)

    print completeness_level_interpolate
    print completeness_level_interpolate_err

    wanted_flux = wanted_flux*1000.0 #make it back to uJy

    mock_catalogue=np.column_stack((wanted_flux, completeness_level_interpolate, completeness_level_interpolate_err))
    np.savetxt('./output/'+cluster_list[l]+'_completeness_level_origflux.cat', mock_catalogue, delimiter=' ', header="flux_uJy completeness_level completeness_level_err") 

    #=============================Plotting=========================================================

    if 0<=l<=4:
        ax=ax_all[0,l]
    elif 5<=l<=9:
        ax=ax_all[1,l-5]
    else:
        ax=ax_all[2,l-10]



    ax.plot(wanted_flux, completeness_level_interpolate, '-o', color='blue', linewidth=2.0, markersize=8.0, label=cluster_list[l])
    #plt.errorbar(random_flux_mJy, completeness_level_median, yerr=completeness_level_std, color='b',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)
    #plt.errorbar(random_flux_mJy, completeness_level_mean, yerr=completeness_level_std, color='r',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)
    ax.errorbar(wanted_flux, completeness_level_interpolate, yerr=completeness_level_interpolate_err, color='b',fmt='o', capsize=5, elinewidth=2,markeredgewidth=2)



    ax.grid()

    leg = ax.legend(handlelength=0, handletextpad=0, fancybox=True, loc='lower right')
    #print leg
    #print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    for item in leg.legendHandles:
        item.set_visible(False)
    leg.get_frame().set_linewidth(0.0)
    leg.get_frame().set_alpha(0.75)



    ax.set_xlim((5.0, 5000.0))
    ax.set_ylim((-0.1, 1.1))
    ax.set_xscale('log')
    #ax.legend(loc=4)
    ax.set_xlabel('Flux density (uJy)')  #==========================================================HERE
    #ax.set_title(cluster_list[0])  #==========================================================HERE
    ax.set_ylabel('Completeness')  #==========================================================HERE
    plt.rc('font', size=15)

    wanted_flux = wanted_flux*0.001 #make it back to mJy

plt.show()




