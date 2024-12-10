import numpy as np
import time

# 100 milyon rastgele sayı içeren bir NumPy dizisi oluşturuyoruz
start_time = time.time()  # Zamanı ölçmeye başla
a = np.random.rand(100000000)

# Dizideki tüm elemanları toplama
total_sum = np.sum(a)
end_time = time.time()  # Zamanı ölçmeyi bitir

# Sonuçları yazdır
print("Toplam:", total_sum)
print("Geçen süre:", end_time - start_time, "saniye")

#NumPy’nin Veriyi Kopyalamaktan Kaçınması
"""
Görünüm (View): NumPy, bazı işlemler için veriyi kopyalamak yerine sadece yeni bir görünüm oluşturur. 
Örneğin, bir matrisin transpozunu aldığınızda NumPy aslında orijinal veriyi kopyalamaz; sadece veri yapısının düzenini
farklı bir şekilde yorumlayarak işlem yapar. Bu sayede hız kazanılır.
"""
# 10,000 x 20,000 boyutunda rastgele sayılarla dolu bir matris oluşturuyoruz
a = np.random.rand(10_000, 20_000)
print(f"Matris `a` bellekte {a.nbytes / 10**6} MB yer kaplıyor")
b = a.transpose()
print("Orijinal Matris (a):\n", a)
print("Transpoze Matris (b):\n", b)

"""
ndarray Yapısının Bellekte Düz 1D Dizi Olarak Saklanması
Kullanıcı Görüşü: Biz matrisi satırlar ve sütunlardan oluşan 2D bir yapı olarak görürüz.
NumPy'nin Görüşü: NumPy, bu 4x4 matrisi bellek içinde [0, 1, 2, ..., 15] şeklinde tek bir uzun dizi olarak saklar.

NumPy, çok boyutlu dizilerde belirli bir elemana erişmek için "raveling" ve "unraveling" adı verilen işlemleri kullanır. 
Bu işlemler, çok boyutlu diziler üzerinde hızlı bir şekilde işlem yapmamıza olanak tanır.

Raveling: Çok boyutlu bir dizinin indekslerini tek boyutlu dizideki karşılık gelen indekslere dönüştürme işlemidir. Örneğin, [2, 3] konumunu tek boyutlu düz dizideki [11] konumuna dönüştürmek.
Unraveling: Ters işlem, yani tek boyutlu bir diziyi çok boyutlu dizi görünümüne çevirme işlemidir. Örneğin, [11] indeksini [2, 3] olarak görmek.

Bu işlemler, NumPy'nin bellekte veriyi kopyalamadan yalnızca dizinin görsel düzenini değiştirmesini sağlar. Bu sayede çok büyük veri kümeleri üzerinde bile hızlı işlem yapılabilir.
"""



# 2x3 boyutunda bir matris oluşturma
a = np.array([[1, 2, 3],
              [4, 5, 6]])

# Kendi ravel fonksiyonumuzu yazalım
def my_ravel(matrix, row, col):
    return row * matrix.shape[1] + col

# [1, 2] konumundaki elemanın 1D düz dizideki karşılığı
print("Raveling sonucu:", my_ravel(a, 1, 2))  # Çıkış 5 olmalı

def ravel(row, col, n_rows, n_cols): #Bu fonksiyon, istenilen elemanın tek boyutlu dizideki indeksini hesaplar.
    return row * n_cols + col

print(ravel(2, 3, n_rows=4, n_cols=4))    # Beklenen çıkış: 11
print(ravel(2, 3, n_rows=4, n_cols=8))    # Beklenen çıkış: 19
print(ravel(0, 0, n_rows=1, n_cols=1))    # Beklenen çıkış: 0
print(ravel(3, 3, n_rows=4, n_cols=4))    # Beklenen çıkış: 15
print(ravel(3465, 18923, n_rows=10000, n_cols=20000))  # Beklenen çıkış: 69318923

"""
NumPy'de bir dizi, bellekte ardışık elemanlar olarak saklanır. Örneğin, 2D bir diziye sahip olduğunuzda, bellekte aslında tek boyutlu bir veri 
bloğu olarak tutulur. strides, bu veri bloğunda dizinin farklı boyutlarında bir sonraki elemana geçmek için kaç bayt atlanması gerektiğini belirtir.
Bir sütundan bir sonraki sütuna geçerken ise sadece 8 bayt atlamak yeterlidir.

"""

# 10,000 x 20,000 boyutunda rastgele bir matris oluşturma
a = np.random.rand(10_000, 20_000)
b = a.transpose()

# Orijinal ve transpoze matrislerin strides değerlerini yazdırma
print("Orijinal matrisin strides değeri:", a.strides)  # (160000, 8)
print("Transpoze matrisin strides değeri:", b.strides)  # (8, 160000)

a = np.random.rand(20_000, 10_000)
print(f'{a.strides=}')  # (80000, 8)
b = a.reshape(40_000, 5_000)
print(f'{b.strides=}')  # (40000, 8)
c = a.reshape(20_000, 5_000, 2)
print(f'{c.strides=}')  # (80000, 16, 8)
