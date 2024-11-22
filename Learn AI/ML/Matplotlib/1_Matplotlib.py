import matplotlib.pyplot as plt
import numpy as np

# fonksiyonel grafik oluşturma
x = np.linspace(0,5,11)
y=x**2
print(x)
print(y)
plt.plot(x,y) # plt.plot(x,y, 'r--') 
plt.show()
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')











