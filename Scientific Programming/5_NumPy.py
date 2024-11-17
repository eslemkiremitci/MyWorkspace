import numpy as np
import time
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Öğe bazında toplama
c = np.add(a, b)
print("a + b işlemi sonucu (np.add):", c)

# Sonucu mevcut bir diziye kaydetme
out_array = np.empty(3)  # Boş bir dizi oluşturuyoruz
print("np.empty(3)", out_array)
np.add(a, b, out=out_array)
print("a + b işlemi sonucu (out argümanı kullanılarak):", out_array)



a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 10, 10])

# Yayılma ile toplama işlemi
c = a + b
print("Yayılma ile toplama işlemi sonucu:\n", c)


x = np.arange(12)
x.shape = (3, 4)
print("Dizi x:\n", x)

# Tüm elemanlar arasındaki en büyük değer
print("x dizisindeki en büyük değer:", x.max())

# Sütunlara göre en büyük değerler
print("Sütunlara göre en büyük değerler:", x.max(axis=0))

# Satırlara göre en büyük değerler
print("Satırlara göre en büyük değerler:", x.max(axis=1))

print("------------------------------------------------------------------------------------------------------------------------------")

# Bir dizi oluşturuyoruz
a = np.array([1, 2, 3, 4])

# Yerinde toplama işlemi (a dizisini kendisiyle toplama)
np.add(a, a, out=a)  # np.add ile a dizisini kendisiyle topluyor ve sonucu yine a dizisine yazıyoruz
print("Yerinde toplama sonucu:", a)

print("------------------------------------------------------------------------------------------------------------------------------")

# Farklı veri tiplerine sahip diziler oluşturuyoruz
a = np.array([1.5, 2.5, 3.5, 4.5], dtype='float64')
b = np.array([1, 1, 1, 1], dtype='int64')

# casting="unsafe" ile dönüşüme izin veriyoruz
np.add(a, b, out=b, casting="unsafe")
print("Yerinde toplama (casting='unsafe') sonucu:", b)

print("------------------------------------------------------------------------------------------------------------------------------")

# Büyük bir dizi oluşturalım
a = np.arange(1000000)

# Zamanlamayı ölçmeden önce işlem
start = time.time()
b = a ** 2
end = time.time()
print("Çıktı argümanı olmadan süre:", end - start)

# Çıktı argümanı kullanarak işlem
b = np.empty_like(a)  # Sonucu saklamak için boş bir dizi oluşturuyoruz
print("b = np.empty_like(a) ",b)
start = time.time()
np.power(a, 2, out=b)  # a**2 işlemi sonucu doğrudan b dizisine yazılır
end = time.time()
print("Çıktı argümanı kullanarak süre:", end - start)

"""
NumPy, kendi matematik rutinlerini icat etmez; bu tür matematik işlemleri 
yapmak için BLAS ve LAPACK gibi kütüphanelere dayanır - birçok dilde olduğu gibi.
"""
print("------------------------------------------------------------------------------------------------------------------------------")

# NumPy’de Lineer Cebir Fonksiyonları
# 2x2 bir kare matris
A = np.array([[1, 2], [3, 4]])

# Matrisin tersi
A_inv = np.linalg.inv(A)
print("Matrisin tersi:\n", A_inv)

# Özdeğerler ve özvektörler
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Özdeğerler:", eigenvalues)
print("Özvektörler:\n", eigenvectors)

# Matrisin determinantı
determinant = np.linalg.det(A)
print("Matrisin determinantı:", determinant)

print("------------------------------------------------------------------------------------------------------------------------------")

arr = np.array([1, 4, 9, 16])
sqrt_arr = np.sqrt(arr)
print("Karekök:", sqrt_arr)

exp_arr = np.exp(arr)
print("Üstel işlem:", exp_arr)

log_arr = np.log(arr)
print("Doğal logaritma:", log_arr)

power_arr = np.power(arr, 2)
print("Üs alma (kare):", power_arr)

mean = np.mean(arr)
print("Ortalama:", mean)

median = np.median(arr)
print("Medyan:", median)

std_dev = np.std(arr)
print("Standart sapma:", std_dev)

variance = np.var(arr)
print("Varyans:", variance)

all_true = np.all(arr)
print("Tüm elemanlar doğru mu?:", all_true)

arr = np.array([False, False, True])
any_true = np.any(arr)
print("En az bir eleman doğru mu?:", any_true)

arr = np.array([1, 2, 3, 4])
indices = np.where(arr > 2)
print("2'den büyük elemanların indeksleri:", indices)


