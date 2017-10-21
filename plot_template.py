import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('Qt5Agg') # specify backend

plt.style.use(os.path.join('Stylesheets', 'matlab_stylesheet.mplstyle'))

data = np.random.randn(50)
plt.plot(data)
plt.show()
