import numpy as np
import matplotlib.pyplot as plotter
import matplotlib.mlab as mlab
import scipy.special as sps

def generate_gamma(shape, m):
    #Parameters of the Gamma distribution
    scale = 1
    dist = np.random.gamma(shape, scale, m)
    est_avg = sum(dist)/m
    act_avg = shape * scale
    return [est_avg, act_avg];

clt = []
for i in range(10000):
    m = 100
    gamma = generate_gamma(2, m)
    clt_value = np.sqrt(m) * (gamma[0] - gamma[1])
    clt.append(clt_value)
    #print clt_value

#print clt
n, bins, patches = plotter.hist(clt, 50, normed=1, facecolor='green', alpha=0.5)
# add a 'best fit' line
y = mlab.normpdf(bins, 0, 1.426)
plotter.plot(bins, y, 'r--')
plotter.subplots_adjust(left=0.15)
plotter.show()

