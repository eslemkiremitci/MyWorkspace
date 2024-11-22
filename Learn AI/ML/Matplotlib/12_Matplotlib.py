import matplotlib.pyplot as plt
import numpy as np
from random import sample


data = sample(range(1, 1000), 100)
plt.hist(data) # dağılım 
plt.show()