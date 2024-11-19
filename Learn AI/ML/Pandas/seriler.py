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
