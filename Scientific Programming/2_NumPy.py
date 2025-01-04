import numpy as np
#NumPy is the most used library for scientific computing.
"""
NumPy Dizilerinin Avantajları:
-NumPy dizileri ise yalnızca tek bir veri türü içerebilir (dtype)
-NumPy dizileri çok boyutlu olabilir.
-NumPy dizileri, ham veri olarak bellekte saklanır (data). Bu veriler, gerektiğinde daha hızlı işlemler 
için C veya Fortran gibi düşük seviyeli dillere aktarılabilir.
"""
a = np.arange(10000) #(10,000 elemanlı) bir NumPy dizisi oluşturuyoruz. 0, 1, 2, ... 9999 olan bir sayı dizisidir.
print(a)
b = np.zeros(10000) # 10,000 elemanlı, başlangıçta tüm elemanları sıfır olan bir NumPy dizisi oluşturuyoruz.
print(b)
b = a ** 2 # 'a' dizisinin her elemanının karesi alınarak 'b' dizisine atanır.
print(b)

#Creating Arrays
a = np.array([1,2,3])# 1 boyutlu dizi (derece 1)
b = np.array([[1,2,3],[4,5,6]])# 2 boyutlu dizi (derece 2)
print(b.shape)# dizinin şekli (satırlar, sütunlar) output = (2, 3)
print(b.size)# eleman sayısı             

print(np.zeros((2, 3)))# Tüm elemanları 0 olan 2x3 dizi
print(np.ones((1, 2)))# Tüm elemanları 1 olan 1x2 dizi
print(np.ones((3, 2), 'bool')) # 3x2 Boolean dizi
print(np.full((2,2),7))# Tüm elemanları 7 olan 2x2 dizi

print(np.eye(4))# 2x2 birim matris
print(np.arange(10))# Belirli bir aralıktaki sayılarla dolu dizi. üç ana parametre alabilir: başlangıç değeri, bitiş değeri, ve adım değeri
print(np.arange(6,100,10))# Belirli bir aralıktaki sayılarla dolu dizi
print(np.linspace(0,9,10))# Aynı aralıktaki değerler, başlangıç değeri, bitiş değeri, ve oluşturulacak eleman sayısı.
print(np.linspace(0,10,20))

#np.save('x.npy', a)       # diziyi bir .npy dosyasına kaydeder
#x = np.load('x.npy')      # bir .npy dosyasından dizi yükleyip x değişkenine atar

print(np.ones((3, 2), 'bool').dtype)# dizinin veri tipi
print(np.ones((3, 2), 'bool').astype('int'))# veri tipini Boolean’dan tamsayıya değiştir

print("---------------------------------------------------------------------------------------------------------------------------")

float_array = np.random.random((3, 2))
print("Ondalıklı sayılardan oluşan dizi:\n", float_array)
int_array = float_array.astype(int)
print("Tam sayılara dönüştürülmüş dizi:\n", int_array)

print("---------------------------------------------------------------------------------------------------------------------------")
# 0 ile 10 arasında rastgele tam sayılardan oluşan 3x2 boyutunda bir dizi oluşturuyoruz
array = np.random.randint(0, 10, (3, 2))
print("Orijinal 3x2 dizi:\n", array)
reshaped_array_2x3 = array.reshape(2, 3) 
# reshape() fonksiyonu, bir dizinin şeklini yeniden düzenlemek için kullanılır 
# ancak dizinin toplam eleman sayısının korunması gerekir.
print("2x3 şeklinde yeniden şekillendirilmiş dizi:\n", reshaped_array_2x3)
reshaped_array_1x6 = array.reshape(1, 6) #
print("1x6 şeklinde yeniden şekillendirilmiş dizi:\n", reshaped_array_1x6)
reshaped_array_6x1 = array.reshape(6, 1)
print("6x1 şeklinde yeniden şekillendirilmiş dizi:\n", reshaped_array_6x1)
reshaped_array_1d = array.reshape(6)#
print("Tek boyutlu (vektör) dizi:\n", reshaped_array_1d)
# Bu geçersiz bir şekillendirme ve hata verir
try:
    reshaped_array_invalid = array.reshape(3, 3)
except ValueError as e:
    print("Geçersiz yeniden şekillendirme hatası:", e)

print("---------------------------------------------------------------------------------------------------------------------------")
array = np.random.randint(0, 10, (3, 2))
print("Orijinal Dizi:\n", array)
np.save('my_array.npy', array)
print("Dizi 'my_array.npy' dosyasına kaydedildi.")
# 'my_array.npy' dosyasından diziyi tekrar yüklüyoruz
loaded_array = np.load('my_array.npy')
print("Dosyadan Yüklenen Dizi:\n", loaded_array)
