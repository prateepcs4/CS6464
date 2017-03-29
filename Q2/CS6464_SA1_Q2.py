import numpy as np
import matplotlib.pyplot as plotter
import scipy.special as sps

#Parameters of the Gamma distribution
shape = 2
scale = 1
m = 100000

dist = np.random.gamma(shape, scale, m)

count, bins, ignored = plotter.hist(dist, 50, normed=True)
y = bins**(shape-1)*(np.exp(-bins/scale) / (sps.gamma(shape)*scale**shape))
plotter.plot(bins, y, linewidth=2, color='r')
plotter.show()
