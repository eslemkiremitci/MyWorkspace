import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10,20,30]
array = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30} #sözlük

#Birinci yöntem
pd.Series(data=my_data) #Serilerde index biz belirleyebilirz
print(pd.Series(data=my_data))
pd.Series(data=my_data, index=labels)

#İkinci yöntem
print(pd.Series(array, labels))

#Üçüncü yöntem
pd.Series(d)
print(pd.Series(d))


print("pd.Series(labels):")
print(pd.Series(labels))

print(pd.Series([print,len,sum])) # python fonk. saklanabilir, referansları tutar. NumPy da yoktur mesela

# Şehir isimleri index
# Veriler plaka numarası. Bu seri türü int64 o nedenle
seri1 = pd.Series([6,16,34,35], ['Ankara', 'Bursa', 'İstanbul', 'İzmir']) 
seri2 = pd.Series([6,38,34,35], ['Ankara', 'Kayseri', 'İstanbul', 'İzmir'])

print(seri1['Ankara'])
print(seri1 + seri2) #float64 artık veri. Veri kaybı olmasın diye.

# -----------------------------------------------------------------------------
# | **Özellik**              | **NumPy Serisi**                                             | **Pandas Serisi**                                             |
# |---------------------------|-------------------------------------------------------------|--------------------------------------------------------------|
# | **Temel Yapı**            | Homojen (aynı veri türü)                                    | Heterojen (farklı veri türlerini barındırabilir)             |
# | **İndeksleme**            | Pozisyon bazlı (0, 1, 2, …)                                | Etiket veya pozisyona dayalı indeksleme                      |
# | **İndeks Özelleştirme**   | Sabit, sayı bazlı                                           | Özelleştirilebilir (string, datetime, vb.)                   |
# | **Eksik Veri Yönetimi**   | Sınırlı (NaN desteklenir ancak manuel işlenir)             | Gelişmiş destek (isna, fillna, dropna gibi metodlarla kolay) |
# | **Hız ve Performans**     | Daha hızlı, hafif                                           | Daha yavaş (daha fazla özellik sunar)                        |
# | **Kullanım Alanı**        | Matematiksel işlemler, bilimsel hesaplamalar               | Veri analizi, manipülasyonu, zaman serisi analizi            |
# | **Matematiksel İşlemler** | Gelişmiş, yüksek performanslı                              | NumPy tabanlı, ancak veri manipülasyonuna odaklıdır          |
# | **Etiketli Veri Desteği** | Yok                                                         | Var                                                          |
# | **Veri Tipi Desteği**     | Tek tip (örneğin sadece float veya int)                    | Bir seride birden fazla veri tipi bulunabilir                |
# | **Çok Boyut Desteği**     | Çok boyutlu diziler desteklenir                            | Tek boyutlu seriler ile sınırlıdır                           |
# | **Veri Manipülasyonu**    | Sınırlı (elle kodlama gerekebilir)                         | Gelişmiş (reindex, merge, groupby gibi araçlarla kolay)      |
# | **Eksik Veri İşleme**     | Yalnızca NaN değerleri ile manuel işleme                  | Doğrudan eksik veri yönetimi araçları sunar                  |
# | **Kütüphane Kapsamı**     | Daha temel bir yapı, Pandas gibi daha gelişmiş kütüphanelere temel oluşturur | Daha yüksek seviyeli veri yapıları ve işlevsellik sağlar     |
# -----------------------------------------------------------------------------
