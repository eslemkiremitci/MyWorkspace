import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y=x**2
# nesne yönelimli grafik oluşturma - daha iyi
fig = plt.figure() # nesne
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')
plt.show()