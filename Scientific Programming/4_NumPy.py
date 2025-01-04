import numpy as np

# 0'dan 15'e kadar olan sayılarla 4x4 matris oluşturma
a = np.arange(16).reshape(4, 4)
print("Dizi a:\n", a)

# İlk satırı seçme
print("İlk satır:", a[0])

# İlk sütunu seçme
print("İlk sütun:", a[:, 0])

# Ortadaki 2x2 alt diziyi seçme
print("Ortadaki 2x2 dizi:\n", a[1:3, 1:3]) # 1. 2. satır sütun.

# Birinci ve ikinci satırın ikinci elemanı
print("Birinci ve ikinci satırın ikinci elemanı:", a[(0, 1), (1, 1)])

# a > 0 koşuluna göre Boolean bir maske oluşturma
idx = (a > 0)
print("Boolean maske:\n", idx)

# Boolean maskeyi kullanarak elemanları seçme
selected_elements = a[idx]
print("Koşula uyan elemanlar:", selected_elements)

# Koşula uyan elemanları tek satırda seçme
selected_elements_one_line = a[a > 0]
print("Tek satırda koşula uyan elemanlar:", selected_elements_one_line)

print("------------------------------------------------------------------------------------------------------------------------------")
# 4x4 birim matrisi oluşturma
a = np.eye(4)
print("Dizi a:\n", a)
# a dizisinin ilk sütununu b olarak atıyoruz
b = a[:, 0]
print("Dizi b (a'nın ilk sütunu):\n", b)
# b dizisinin ilk elemanını 5 olarak değiştiriyoruz
b[0] = 5
print("Dizi b güncellendikten sonra b:\n", b)
print("Dizi b güncellendikten sonra a:\n", a)

"""
b[0] = 5 ifadesi a dizisini etkiliyor çünkü b dizisi, a dizisinin bir görünümü (view) olarak tanımlandı. 
NumPy’de bir dizi üzerinde dilimleme (a[:, 0] gibi) yaptığınızda, bu dilim orijinal dizinin bir parçasını temsil eden 
bir görünüm olur. Yani, b, a dizisinin ilk sütununu gösteren bir referanstır, bağımsız bir kopya değildir.
"""

# Görünüm (View) ile Kopya (Copy) Arasındaki Fark
# a dizisinin ilk sütununun bağımsız bir kopyasını oluşturma
b = a[:, 0].copy()
b[0] = 4
print("Dizi b güncellendikten sonra b (kopya):\n", b)
print("Dizi b güncellendikten sonra a (orijinal):\n", a)

"""
b, a dizisinin bir görünümü olduğu için b üzerindeki değişiklikler a dizisini etkiledi. 
Eğer b'yi a dizisinden bağımsız bir kopya olarak oluşturmak istiyorsa, copy() fonksiyonunu kullanılabilir.
"""

