import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y=x**2

fig = plt.figure(figsize=(8,2))
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
plt.show()