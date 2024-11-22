import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y=x**2

fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(x,y)
axes1.set_title('Büyük Grafik')
axes2.plot(y,x)
axes2.set_title('Küçük Grafik')
plt.show()