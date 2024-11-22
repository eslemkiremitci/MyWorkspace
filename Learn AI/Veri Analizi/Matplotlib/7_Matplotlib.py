import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y=x**2

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout() # sayıların grafiğin arkasında olmasını engeller
plt.show()
fig.savefig(r'C:\Users\eslem\OneDrive\Masaüstü\MyWorkspace\Learn AI\ML\Matplotlib\1.jpg')