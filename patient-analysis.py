""" Patient's inflammation analysis for day 1"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname = 'data/inflammation-01.csv',delimiter =',')

#Finding dimensions of data
print(data.shape)

#Plotting Data
image-1 = plt.plot(data)

plt.show(image-1)
