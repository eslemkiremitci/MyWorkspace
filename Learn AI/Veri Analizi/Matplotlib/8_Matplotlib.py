import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y=x**2

# legend grafik hakkında bilgi veren genelde grafiğin köşesine eklenen bilgi kutucuğu  
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label='x kare')
ax.plot(x,x**3, label='x küp')
ax.legend(loc=(0.2, 0.4))
plt.show()
