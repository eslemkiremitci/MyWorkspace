import numpy as np

# Örnek vektör
arr = np.array([1, 2, 3])

# Ters çevirme
reversed_arr = arr[::-1]
print("Ters çevrilmiş vektör:", reversed_arr)

arr = np.ones((5, 5))
arr[0, :] = 0
arr[-1, :] = 0
arr[:, 0] = 0
arr[:, -1] = 0
print("Kenarları 0, içi 1 olan dizi:\n", arr)

arr = np.random.rand(5, 5)
#NumPy kütüphanesinde rastgele bir boyutta 0 ile 1 arasında (1 dahil değil) eşit olasılıkla 
# dağıtılmış on adet kayan nokta sayıdan oluşan bir dizi oluşturur.
print(arr)
arr[(arr >= 0.2) & (arr <= 0.7)] += 10
print("Belirli aralıktaki elemanlara 10 eklenmiş dizi:\n", arr)

print("np.round(0.5):", np.round(0.5))  # 0
print("np.round(1.5):", np.round(1.5))  # 2

arr = np.array([-1.5, -0.5, 0.5, 1.5])

print("np.ceil:", np.ceil(arr))    # En yakın tam sayıya yukarı yuvarlar
print("np.floor:", np.floor(arr))  # En yakın tam sayıya aşağı yuvarlar
print("np.trunc:", np.trunc(arr))  # Ondalık kısmı keser

arr = np.random.rand(10)
sorted_arr = np.sort(arr)
print("Sıralanmış dizi:", sorted_arr)

#Dolaylı sıralama, bir dizinin sıralı düzene göre indekslerini verir.
arr = np.random.rand(10)
indices = np.argsort(arr)
print("Sıralı indeksler:", indices)
print("Sıralı dizi:", arr[indices])


zeros = np.zeros((4, 4))
ones = np.ones((4, 4))

# Sıfırlar üstte, birler altta (8x4)
vertical_stack = np.vstack((zeros, ones))
print("Dikey birleştirme (8x4):\n", vertical_stack)

# Sıfırlar solda, birler sağda (4x8)
horizontal_stack = np.hstack((zeros, ones))
print("Yatay birleştirme (4x8):\n", horizontal_stack)

import time
a = np.random.rand(100, 100)
print(a)
b = np.random.rand(100, 100)

# Manuel matris çarpımı (döngü ile)
start = time.time()
result_manual = np.zeros((100, 100))
for i in range(100):
    for j in range(100):
        for k in range(100):
            result_manual[i, j] += a[i, k] * b[k, j]
end = time.time()
print("Manuel matris çarpımı süresi:", end - start)

# np.dot ile matris çarpımı
start = time.time()
result_dot = np.dot(a, b)
end = time.time()
print("np.dot ile matris çarpımı süresi:", end - start)
