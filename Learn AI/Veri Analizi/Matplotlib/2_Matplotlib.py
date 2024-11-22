import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y=x**2
plt.subplot(1,2,1) # birden fazla grafik oluşturma - sttır -sütun - index
plt.plot(x,y,'r') #red
plt.subplot(1,2,2) # ikinci  grafik
plt.plot(y,x,'b') #blue -  tam tersi 
plt.show()