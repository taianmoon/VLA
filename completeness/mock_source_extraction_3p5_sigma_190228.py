from astropy.io import fits
import astropy.wcs as wcs
import numpy as np


#============================Transform all pixel values and coordinates into lists=======================

hdulist = fits.open('./output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_snr_170919.fits')      #================================================================================HERE
w = wcs.WCS(hdulist[0].header, hdulist)
naxis1=hdulist[0].header['NAXIS1']
naxis2=hdulist[0].header['NAXIS2']
scidata = hdulist[0].data
hdulist.close()

hdulist_flux = fits.open('./output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_flux_170919.fits')      #================================================================================HERE
w_flux = wcs.WCS(hdulist_flux[0].header, hdulist_flux)
scidata_flux = hdulist_flux[0].data
hdulist_flux.close()

#print hdulist[0].header['NAXIS1']
#print hdulist[0].header['NAXIS2']


#print w_flux
#print scidata_flux[0,100,:]
#print np.shape(scidata_flux)

#print w
#print scidata[0,174,:]
#print np.shape(scidata)



pix_coor_x=[]
pix_coor_y=[]
pix_value_array=[]
pix_value_flux_array=[]
for i in range(0, naxis2):
    for j in range(0, naxis1):
        #pix_value_array.append(scidata[0,i,j])   #======================================================HERE(Orz): ([0,i,j] for ordinary fields; [i,j] for S2COSMOS)
        #pix_value_flux_array.append(scidata_flux[0,i,j])
        pix_value_array.append(scidata[i,j])
        pix_value_flux_array.append(scidata_flux[i,j])
        pix_coor_x.append(j+1)
        pix_coor_y.append(i+1)


#print pix_value_array
#print pix_value_flux_array
#print pix_coor_x
#print pix_coor_y

#print pix_value_flux_array[88]
#print pix_value_array[88]
#print pix_coor_x[88]
#print pix_coor_y[88]

#print np.size(pix_value_array)
#print np.size(pix_coor_x)
#print np.size(pix_coor_y)


#=======================Filter out sigma>3 pixels====================================================

pix_value_array_3sigma=[]
pix_value_flux_array_3sigma=[]
pix_coor_x_3sigma=[]
pix_coor_y_3sigma=[]
for k in range(0, len(pix_value_array)):

    if pix_value_array[k] >= 5.0:                           #================================================================================HERE: 3.5-sigma?

        pix_value_array_3sigma.append(pix_value_array[k])
        pix_value_flux_array_3sigma.append(pix_value_flux_array[k])
        pix_coor_x_3sigma.append(pix_coor_x[k])
        pix_coor_y_3sigma.append(pix_coor_y[k])

#print pix_value_array_3sigma[100]
#print pix_value_flux_array_3sigma
#print pix_coor_x_3sigma
#print pix_coor_y_3sigma


#print np.size(pix_value_array_3sigma)
#print np.size(pix_coor_x_3sigma)
#print np.size(pix_coor_y_3sigma)


if pix_value_array_3sigma:
    pix_value_array_3sigma_sorted, pix_value_flux_array_3sigma_sorted, pix_coor_x_3sigma_sorted, pix_coor_y_3sigma_sorted = (list(t) for t in zip(*sorted(zip(pix_value_array_3sigma, pix_value_flux_array_3sigma, pix_coor_x_3sigma, pix_coor_y_3sigma))))
else:
    pix_value_array_3sigma_sorted = []
    pix_value_flux_array_3sigma_sorted = []
    pix_coor_x_3sigma_sorted = []
    pix_coor_y_3sigma_sorted = []


pix_value_array_3sigma_sorted=pix_value_array_3sigma_sorted[::-1]
pix_value_flux_array_3sigma_sorted=pix_value_flux_array_3sigma_sorted[::-1]
pix_coor_x_3sigma_sorted=pix_coor_x_3sigma_sorted[::-1]
pix_coor_y_3sigma_sorted=pix_coor_y_3sigma_sorted[::-1]


#print pix_value_array_3sigma_sorted
#print pix_value_flux_array_3sigma_sorted
#print pix_coor_x_3sigma_sorted
#print pix_coor_y_3sigma_sorted


#print np.size(pix_value_array_3sigma_sorted)
#print np.size(pix_coor_x_3sigma_sorted)
#print np.size(pix_coor_y_3sigma_sorted)



#======================Perform flood-fill algorithm and mask out neighbouring pixels===================

pix_value_array_3sigma_sorted_extract=[]
pix_value_flux_array_3sigma_sorted_extract=[]
pix_coor_x_3sigma_sorted_extract=[]
pix_coor_y_3sigma_sorted_extract=[]



#pix_coor_x
#pix_coor_y
#pix_value_array
#pix_value_flux_array
#scidata[0,:,:]
#scidata_flux[0,:,:]
def floodfill(x,y):
    

    # assume surface is a 2D image and surface[x][y] is the color at x, y.

    if scidata[y-1,x-1] < 5.0: # the base case      #================================================================================HERE: 3.5-sigma?
    #if scidata[y-1,x-1] < 3.5: # the base case      #================================================================================HERE: 3.5-sigma? (Orz) S2CLS

        return; 

    pix_value_array_3sigma_sorted_extract_tmp.append(scidata[y-1,x-1])
    scidata[y-1,x-1] = 0.0
    #pix_value_array_3sigma_sorted_extract_tmp.append(scidata[y-1,x-1])  #============================================================HERE (Orz) S2CLS
    #scidata[y-1,x-1] = 0.0


    floodfill(x + 1, y) # right

    floodfill(x - 1, y) # left

    floodfill(x, y + 1) # up

    floodfill(x, y - 1) # down

    floodfill(x + 1, y+1) # right-up

    floodfill(x + 1, y-1) # right-down

    floodfill(x-1, y + 1) # left-up

    floodfill(x-1, y - 1) # left-down



for m in range(0, len(pix_value_array_3sigma_sorted)):
#for m in range(0, 2):

    pix_value_array_3sigma_sorted_extract_tmp=[]
    try:
        
        floodfill(pix_coor_x_3sigma_sorted[m],pix_coor_y_3sigma_sorted[m])
        #pix_value_array_3sigma_sorted_extract.append(scidata[0,pix_coor_y_3sigma_sorted[m]-1,pix_coor_x_3sigma_sorted[m]-1])
        #pix_value_flux_array_3sigma_sorted_extract.append(scidata_flux[0,pix_coor_y_3sigma_sorted[m]-1,pix_coor_x_3sigma_sorted[m]-1])
        #pix_coor_x_3sigma_sorted_extract.append(pix_coor_x_3sigma_sorted[m])
        #pix_coor_y_3sigma_sorted_extract.append(pix_coor_y_3sigma_sorted[m])


    except:
        print "source near the edge"
        #and then append a new list with this first starting pixel
        #pix_value_array_3sigma_sorted_extract.append(scidata[0,pix_coor_y_3sigma_sorted[m]-1,pix_coor_x_3sigma_sorted[m]-1])
        #pix_value_flux_array_3sigma_sorted_extract.append(scidata_flux[0,pix_coor_y_3sigma_sorted[m]-1,pix_coor_x_3sigma_sorted[m]-1])
        #pix_coor_x_3sigma_sorted_extract.append(pix_coor_x_3sigma_sorted[m])
        #pix_coor_y_3sigma_sorted_extract.append(pix_coor_y_3sigma_sorted[m])

    if pix_value_array_3sigma_sorted_extract_tmp:
        pix_value_array_3sigma_sorted_extract.append(pix_value_array_3sigma_sorted_extract_tmp[0])
        pix_value_flux_array_3sigma_sorted_extract.append(scidata_flux[pix_coor_y_3sigma_sorted[m]-1,pix_coor_x_3sigma_sorted[m]-1])
        #pix_value_flux_array_3sigma_sorted_extract.append(scidata_flux[pix_coor_y_3sigma_sorted[m]-1,pix_coor_x_3sigma_sorted[m]-1])   #=========================================HERE (Orz) S2CLS
        pix_coor_x_3sigma_sorted_extract.append(pix_coor_x_3sigma_sorted[m])
        pix_coor_y_3sigma_sorted_extract.append(pix_coor_y_3sigma_sorted[m])
        #print pix_value_array_3sigma_sorted_extract_tmp[0]
  


pix_value_array_3sigma_sorted_extract = np.array(pix_value_array_3sigma_sorted_extract)
pix_value_array_3sigma_sorted_extract=np.array([float(i) for i in pix_value_array_3sigma_sorted_extract])
pix_value_flux_array_3sigma_sorted_extract = np.array(pix_value_flux_array_3sigma_sorted_extract)
pix_value_flux_array_3sigma_sorted_extract=np.array([float(i) for i in pix_value_flux_array_3sigma_sorted_extract])

pix_value_flux_array_3sigma_sorted_extract_mJy=pix_value_flux_array_3sigma_sorted_extract*1000.0  #================================================================HERE (Orz) ordinary fields: in mJy
#pix_value_flux_array_3sigma_sorted_extract_mJy=pix_value_flux_array_3sigma_sorted_extract*1.0*1.0     #================================================================HERE (Orz) S2CLS

pix_value_flux_array_3sigma_sorted_extract_mJy = np.array(pix_value_flux_array_3sigma_sorted_extract_mJy)
pix_value_flux_array_3sigma_sorted_extract_mJy=np.array([float(i) for i in pix_value_flux_array_3sigma_sorted_extract_mJy])




#print pix_value_array_3sigma_sorted_extract  #S/N
#print pix_value_flux_array_3sigma_sorted_extract  #flux in pW
#print pix_value_flux_array_3sigma_sorted_extract_mJy #flux in mJy/beam

pix_value_flux_error_array_3igma_sorted_extract_mJy=pix_value_flux_array_3sigma_sorted_extract_mJy/pix_value_array_3sigma_sorted_extract
pix_value_flux_error_array_3igma_sorted_extract_mJy = np.array(pix_value_flux_error_array_3igma_sorted_extract_mJy)
pix_value_flux_error_array_3igma_sorted_extract_mJy=np.array([float(i) for i in pix_value_flux_error_array_3igma_sorted_extract_mJy])
#print pix_value_flux_error_array_3igma_sorted_extract_mJy  #flux error in mJy

#print pix_coor_x_3sigma_sorted_extract
#print pix_coor_y_3sigma_sorted_extract
#print scidata[0,78,94]
#print scidata[0,78,95]
#print scidata[0,78,93]
#print scidata[0,78,92]
#print scidata[0,77,94]
#print scidata[0,79,94]
#print scidata[0,77,95]
#print scidata[0,79,95]
#print scidata[0,77,93]
#print scidata[0,77,92]

#print scidata[0,67,82]





#floodfill(95,79,pix_value_array_3sigma_sorted[0])
#-----------------------------------------------------------------------------------------------------

#pix_value_array_3sigma_sorted[0]=7.7916966433753165
#[95,79]

#pix_value_array_3sigma_sorted_extract=[]
#pix_coor_x_3sigma_sorted_extract=[]
#pix_coor_y_3sigma_sorted_extract=[]


#pix_value_array_3sigma_sorted_extract.append(pix_value_array_3sigma_sorted[0])
#pix_coor_x_3sigma_sorted_extract.append(pix_coor_x_3sigma_sorted[0])
#pix_coor_y_3sigma_sorted_extract.append(pix_coor_y_3sigma_sorted[0])

#for n in range(0, len(pix_value_array_3sigma_sorted)):

#    if (pix_coor_x_3sigma_sorted[n]-pix_coor_x_3sigma_sorted[0])**2+(pix_coor_y_3sigma_sorted[n]-pix_coor_y_3sigma_sorted[0])**2 <= 1.0:
##        don't append, and then assign to 0
#        pix_value_array_3sigma_sorted[0]=0.0
#        pix_value_array_3sigma_sorted[n]=0.0
#    else:
##        append, and then assign to 0
#        pix_value_array_3sigma_sorted_extract.append(pix_value_array_3sigma_sorted[n])
#        pix_value_array_3sigma_sorted[0]=0.0

##    sort again before the next iteration


#pix_value_array_3sigma_sorted, pix_value_flux_array_3sigma_sorted, pix_coor_x_3sigma_sorted, pix_coor_y_3sigma_sorted = (list(t) for t in zip(*sorted(zip(pix_value_array_3sigma, pix_value_flux_array_3sigma, pix_coor_x_3sigma, pix_coor_y_3sigma))))




#=================================Convert pixel coordinates to ra, decs of the selected sources======================

#ra_3sigma_sorted_extract=[]
#dec_3sigma_sorted_extract=[]
#for o in range(0, len(pix_coor_x_3sigma_sorted_extract)):
#
#    s1, ignore = w.all_pix2world([[pix_coor_x_3sigma_sorted_extract[o],pix_coor_y_3sigma_sorted_extract[o],1],[0,0,0]],1)
#    #ra, dec = w.all_pix2world([20,30,0], 1 )
#
#    radec_list=[s1]
#
#
#    #for n in range(0, len(s1)):
#    ra_3sigma_sorted_extract.append(s1[0])
#    dec_3sigma_sorted_extract.append(s1[1])
#
#    #ra_tmp = [item[0] for item in radec_list]
#    #dec_tmp = [item[1] for item in radec_list]
#
##ra=[s1[0],s2[0]]
##dec=[s1[1],s2[1]]
#
#
#
#ra_3sigma_sorted_extract = np.array(ra_3sigma_sorted_extract)
#ra_3sigma_sorted_extract=np.array([float(i) for i in ra_3sigma_sorted_extract])
#dec_3sigma_sorted_extract = np.array(dec_3sigma_sorted_extract)
#dec_3sigma_sorted_extract=np.array([float(i) for i in dec_3sigma_sorted_extract])
#
#
#
##print ra_3sigma_sorted_extract
##print dec_3sigma_sorted_extract
##print s1
##print s2
##print ignore
#
#



#===============================================Stacke all lists together and output source catalogue===========================

mock_catalogue=np.column_stack((pix_coor_x_3sigma_sorted_extract, pix_coor_y_3sigma_sorted_extract, pix_value_array_3sigma_sorted_extract, pix_value_flux_array_3sigma_sorted_extract, pix_value_flux_array_3sigma_sorted_extract_mJy, pix_value_flux_error_array_3igma_sorted_extract_mJy))

np.savetxt('./output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_3p5sigma.cat', mock_catalogue, delimiter=' ', header="pix_x pix_y SN_ratio flux_pW flux_mJy_perbeam flux_error_mJy") #================================================================================HERE



#mock_catalogue_ds9=np.column_stack((ra_3sigma_sorted_extract, dec_3sigma_sorted_extract))
#
#np.savetxt('./output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_3p5sigma.reg', mock_catalogue_ds9, delimiter=' ') #================================================================================HERE









