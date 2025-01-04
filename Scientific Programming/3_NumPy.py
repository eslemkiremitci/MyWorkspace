import numpy as np
"""
Vektörleştirme, NumPy’nin döngü yazmanıza gerek kalmadan tüm dizi elemanları üzerinde işlemler yapabilmesini ifade eder.
Bu, her bir eleman için ayrı ayrı işlem yapmak yerine, tüm elemanların aynı anda işlenmesini sağlar.
"""
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

# Öğe bazında toplama
c = a + b
print("Öğe bazında toplama:\n", c)

# Öğe bazında toplama (np.add kullanarak)
d = np.add(a, b)
print("np.add kullanarak toplama:\n", d)

# Matris çarpımı
e = a @ b
print("Matris çarpımı (@ ile):\n", e)

# Matris çarpımı (np.dot kullanarak)
f = np.dot(a, b)
print("Matris çarpımı (np.dot kullanarak):\n", f)

# Çıkarma (Subtraction)
subtraction_result = np.subtract(a, b)
print("Çıkarma işlemi sonucu (a - b):\n", subtraction_result)

# Bölme (Division)
division_result = np.divide(a, b)
print("Bölme işlemi sonucu (a / b):\n", division_result)

# Transpoz (Transpose)
transpose_result = a.T
print("a dizisinin transpozu:\n", transpose_result)

# Karekök (Square Root)
sqrt_result = np.sqrt(a)
print("a dizisinin her elemanının karekökü:\n", sqrt_result)

# Tüm elemanların toplamı
total_sum = np.sum(a)
print("a dizisindeki tüm elemanların toplamı:", total_sum)

# Satırlara göre toplam (axis=1)
row_sum = np.sum(a, axis=1)
print("Satırlara göre toplam:\n", row_sum)

# Sütunlara göre toplam (axis=0)
column_sum = np.sum(a, axis=0)
print("Sütunlara göre toplam:\n", column_sum)

"""
numpy.multiply, iki diziyi öğe bazında (element-wise) çarpmak
için kullanılır. Yani, dizilerin aynı konumda olan elemanları birbiriyle çarpılır.
"""
# Öğeler bazında çarpma
element_wise_multiplication = np.multiply(a, b)
print("Öğe bazında çarpma (np.multiply):\n", element_wise_multiplication)

"""
numpy.dot, matris çarpımı yapmak için kullanılır. Matris çarpımı, 
matematiksel olarak iki matrisin satır ve sütunları arasındaki özel bir çarpma işlemidir.
Bu işlemde, a matrisinin satırları ile b matrisinin sütunları çarpılarak ve toplanarak sonuç matrisinin elemanları bulunur.
"""

# Matris çarpımı
matrix_multiplication = np.dot(a, b)
print("Matris çarpımı (np.dot):\n", matrix_multiplication)

# Sütunlara göre toplam (axis=0)
column_sum = np.sum(a, axis=0)
print("Sütunlara göre toplam (axis=0):\n", column_sum)

# Satırlara göre toplam (axis=1)
row_sum = np.sum(a, axis=1)
print("Satırlara göre toplam (axis=1):\n", row_sum)

# Tüm elemanların toplamı (axis belirtilmemiş)
total_sum = np.sum(a)
print("Tüm elemanların toplamı (axis belirtilmemiş):", total_sum)






