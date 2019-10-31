






for l in range(0, len(cluster_list)):    #================loop over clusters

    #print cluster_list[l]


    #hdulist_flux = fits.open('./'+cluster_list[l]+'/'+cluster_list[l]+'_flux_170919.fits')      #================================================================================HERE
    #w_flux = wcs.WCS(hdulist_flux[0].header, hdulist_flux)
    #NAXIS1_flux=hdulist_flux[0].header['NAXIS1']
    #NAXIS2_flux=hdulist_flux[0].header['NAXIS2']
    #CDELT1_flux=hdulist_flux[0].header['CDELT1']
    #CDELT2_flux=hdulist_flux[0].header['CDELT2']
    #scidata_flux = hdulist_flux[0].data  #================flux: unit of pW
    #hdr = hdulist_flux[0].header
    #hdulist_flux.close()


    #hdulist_noise_2 = fits.open('../'+cluster_list[l]+'/'+cluster_list[l]+'_VLA_rms_crop.fits')      #================================================================================HERE
    hdulist_noise_2 = fits.open('../'+cluster_list[l]+'/'+cluster_list[l]+'_crop_rms_sqaure_small.fits')      #================================================================================HERE
    w_noise_2 = wcs.WCS(hdulist_noise_2[0].header, hdulist_noise_2)
    NAXIS1_noise=hdulist_noise_2[0].header['NAXIS1']
    NAXIS2_noise=hdulist_noise_2[0].header['NAXIS2']
    CDELT1_noise=hdulist_noise_2[0].header['CDELT1']
    CDELT2_noise=hdulist_noise_2[0].header['CDELT2']
    #scidata_noise_2 = np.sqrt(hdulist_noise_2[0].data)  #================variance: unit of Jy
    scidata_noise_2 = hdulist_noise_2[0].data  #================variance: unit of Jy
    hdulist_noise_2.close()



    #print scidata_flux[0, 100, 100]


    #random_positions_x_long=[]
    #random_positions_y_long=[]
    #for i in range(100):
    #    x_tmp=random.randint(1,NAXIS1_flux-1)
    #    y_tmp=random.randint(1,NAXIS2_flux-1)
    #    if np.isnan(scidata_flux[0, y_tmp, x_tmp])==False:
    #        random_positions_x_long.append(x_tmp)
    #        random_positions_y_long.append(y_tmp)

    #random_positions_x = random_positions_x_long[0:10]
    #random_positions_y = random_positions_y_long[0:10]


    #print random_positions_x
    #print random_positions_y
    #print len(random_positions_x)
    #print len(random_positions_y)
    #print '1111111111111111111111'






    #completeness_level=[]  #in percentage
    for rf in range(0, len(random_flux)):  #==================loop over different flux
        #print random_flux_mJy[rf]
        #print 'flux!!'
        #execfile("./completeness_190226.py")
        execfile("./completeness_detail_190301.py")
        #execfile("./mock_source_extraction_3p5_sigma_190228.py")
        os.system('python2 /home/tc1815/Blobcat/blobcat.py ./output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_flux_170919.fits --rmsmap ../'+cluster_list[l]+'/'+cluster_list[l]+'_crop_rms_sqaure_small.fits --write --ds9')
        
        
        #fname_mock = './output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_3p5sigma.cat'
        fname_mock = './output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_flux_170919_blobs.txt'
        #fname_orig = '../'+cluster_list[l]+'/Blobcat_source_detection/uniform_noise/cat_cut.txt'

        #fname_orig = '../'+cluster_list[l]+'/cat_cut.txt'
        fname_orig = '../'+cluster_list[l]+'/'+cluster_list[l]+'_crop_sqaure_small_blobs.txt'
        
        num_lines_mock = 0
        with open(fname_mock, 'r') as f_mock:
           for line_mock in f_mock:
               num_lines_mock += 1
        #print "Number of lines mock:"
        #print random_flux_mJy[rf]
        #print num_lines_mock
        
        
        num_lines_orig = 0
        with open(fname_orig, 'r') as f_orig:
           for line_orig in f_orig:
               num_lines_orig += 1
        #print "Number of lines orig:"
        #print num_lines_orig
        
        if random_flux_mJy_int[rf] == 0.010:
           completeness_level_2.append(abs(num_lines_mock-num_lines_orig)/float(len(random_positions_x)))
           completeness_level_cumulative_loop_2 = completeness_level_cumulative_loop_2 + abs(num_lines_mock-num_lines_orig)
        elif random_flux_mJy_int[rf] == 0.030:
           completeness_level_4.append(abs(num_lines_mock-num_lines_orig)/float(len(random_positions_x)))
           completeness_level_cumulative_loop_4 = completeness_level_cumulative_loop_4 + abs(num_lines_mock-num_lines_orig)
        elif random_flux_mJy_int[rf] == 0.068:
           completeness_level_6.append(abs(num_lines_mock-num_lines_orig)/float(len(random_positions_x)))
           completeness_level_cumulative_loop_6 = completeness_level_cumulative_loop_6 + abs(num_lines_mock-num_lines_orig)
        elif random_flux_mJy_int[rf] == 0.096:
           completeness_level_8.append(abs(num_lines_mock-num_lines_orig)/float(len(random_positions_x)))
           completeness_level_cumulative_loop_8 = completeness_level_cumulative_loop_8 + abs(num_lines_mock-num_lines_orig)
        elif random_flux_mJy_int[rf] == 0.135:
           completeness_level_10.append(abs(num_lines_mock-num_lines_orig)/float(len(random_positions_x)))
           completeness_level_cumulative_loop_10 = completeness_level_cumulative_loop_10 + abs(num_lines_mock-num_lines_orig)
        elif random_flux_mJy_int[rf] == 0.206:
           completeness_level_12.append(abs(num_lines_mock-num_lines_orig)/float(len(random_positions_x)))
           completeness_level_cumulative_loop_12 = completeness_level_cumulative_loop_12 + abs(num_lines_mock-num_lines_orig)
        elif random_flux_mJy_int[rf] == 0.368:
           completeness_level_14.append(abs(num_lines_mock-num_lines_orig)/float(len(random_positions_x)))
           completeness_level_cumulative_loop_14 = completeness_level_cumulative_loop_14 + abs(num_lines_mock-num_lines_orig)
        elif random_flux_mJy_int[rf] == 0.589:
           completeness_level_16.append(abs(num_lines_mock-num_lines_orig)/float(len(random_positions_x)))
           completeness_level_cumulative_loop_16 = completeness_level_cumulative_loop_16 + abs(num_lines_mock-num_lines_orig)
        elif random_flux_mJy_int[rf] == 1.084:
           completeness_level_18.append(abs(num_lines_mock-num_lines_orig)/float(len(random_positions_x)))
           completeness_level_cumulative_loop_18 = completeness_level_cumulative_loop_18 + abs(num_lines_mock-num_lines_orig)
        elif random_flux_mJy_int[rf] == 1.802:
           completeness_level_20.append(abs(num_lines_mock-num_lines_orig)/float(len(random_positions_x)))
           completeness_level_cumulative_loop_20 = completeness_level_cumulative_loop_20 + abs(num_lines_mock-num_lines_orig)
        
        
        
        
        #completeness_level.append(abs(num_lines_mock-num_lines_orig)/float(len(random_positions_x)))
        #print abs(num_lines_mock-num_lines_orig)/float(len(random_positions_x))
        #print len(random_positions_x)
        #print 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
        
        if random_flux_mJy_int[rf] != 0.206 or rt != realization_times-1:
            #os.remove('./output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_3p5sigma.cat')
            os.remove('./output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_flux_170919.fits')
            os.remove('./output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_snr_170919.fits')
            #os.remove('./output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_3p5sigma.reg')

            os.remove('./output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_flux_170919_blobs.txt')
            os.remove('./output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_flux_170919_blobs.fits')
            os.remove('./output/mock_'+str(random_flux_mJy_int[rf])+'mJy_'+cluster_list[l]+'_flux_170919_ds9.reg')
        

    #print completeness_level_2
    #print completeness_level_4
    #print completeness_level_6
    #print completeness_level_8
    #print completeness_level_10
    #print completeness_level_12
    #print completeness_level_14
    #print completeness_level_16
    #print completeness_level_18
    #print completeness_level_20
    #print 'xxxxxxxxxxxxxxxxxxxxxxxxxx'





    #completeness_catalogue=np.column_stack((random_flux_mJy, completeness_level))

    #np.savetxt('./'+cluster_list[l]+'/'+cluster_list[l]+'_completeness_level.cat', completeness_catalogue, delimiter=' ', header="flux_mJy completeness") #================================================================================HERE






