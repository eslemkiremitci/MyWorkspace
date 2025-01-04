import numpy as np
from numpy.lib.stride_tricks import as_strided
"""
numpy.lib.stride_tricks.as_strided() fonksiyonu, bir NumPy dizisini farklı bir shape ve strides ile yeni bir 
görünüm olarak sunmamıza olanak tanır. Bu, veriyi kopyalamadan, bellekteki aynı veriyi farklı bir şekilde yorumlamamızı sağlar.
Örneğin, bir diziyi transpoze etmek veya yeniden şekillendirmek için bu fonksiyon kullanılabilir.
"""

def my_transpose(arr):
    # shape ve strides değerlerini ters çevirerek transpoz yapıyoruz
    return as_strided(arr, shape=(arr.shape[1], arr.shape[0]), strides=(arr.strides[1], arr.strides[0]))

# 2x3 boyutunda örnek bir dizi
a = np.array([[1, 2, 3], [4, 5, 6]])
b = my_transpose(a)

print("Orijinal dizi:\n", a)
print("Transpoze edilmiş dizi:\n", b)

# 1D bir dizi oluşturuyoruz
a = np.array([1., 2., 3., 4., 5.])

# `shape` ve `strides` özniteliklerini ayarlayarak 2D görünümü elde ediyoruz
b = as_strided(a, shape=(5, 1000000000000), strides=(a.strides[0], 0))

print("İstenen 2D matris:\n", b)

