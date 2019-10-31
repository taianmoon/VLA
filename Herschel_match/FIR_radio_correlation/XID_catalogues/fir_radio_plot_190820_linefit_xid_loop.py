import pyfits
import matplotlib.pyplot as plt
import numpy as np
import math
import glob
import os.path


cluster_list=['Bootes1', 'Lockman', 'G12', 'NGP1', 'NGP3', 'NGP5', 'NGP6', 'NGP7', 'NGP9', 'G018']
#cluster_list=['bootes1']


fig, ax_all =plt.subplots(5,2, figsize=(16.0, 10.0), sharex=True, sharey=True)

for l in range(0, len(cluster_list)):

    print cluster_list[l]
    execfile("./fir_radio_plot_190820_linefit.py")


plt.rc('font', size=20)
plt.show()
