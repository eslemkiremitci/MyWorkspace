import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y=x**2

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

                     
ax.plot(x,y,color='red', lw=3, ls='--', marker='o', ms=30, markerfacecolor='yellow',
       markeredgewidth=8, markeredgecolor='purple')
plt.show()

# lw kalınlık 
# ls grafik yapısı -- , -. , : , steps , 
# marker 11 noktanın olduğu yere işaret koyma ms marker büyüklüğü
# marker iç rengi markerfacecolor='yellow',
# marker dış renk  markeredgecolor='purple')
# marker kalınlığı markeredgewidth=8,