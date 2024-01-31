import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as stats
np.random.seed(0)
mean = 90
deviation = 25
x = mean + deviation * np.random.randn(500)
num_bins = 10
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=1)
y = stats.norm.pdf(bins, mean, deviation)
ax.plot(bins, y, '--')
ax.set_xlabel('Example Data')
ax.set_ylabel('Probability density')
Title='Histogram'
ax.set_title(Title)
fig.tight_layout()
plt.show()
#bins define the interval, density=1 is used for smooth kernel plotting
#tight_layout automatically adjusts subplot parameters
#patches is used for edges color
