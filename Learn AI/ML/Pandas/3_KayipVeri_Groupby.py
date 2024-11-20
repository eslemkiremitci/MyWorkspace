import numpy as np
import pandas as pd

print("Kayıp Veriler")

d = {'A': [1,2,np.nan], 'B': [np.nan,3,np.nan], 'C': [4,5,6]}
df = pd.DataFrame(d)
print("\n \n",df)

df.dropna()
print("\n \n",df.dropna())#kayıp veri olanları full siler
print("\n \n",df)

df.dropna(axis=1)
print("\n \n",df.dropna(axis=1)) #sütun
print("\n \n",df)

df.dropna(thresh=2)
print("\n \n",df.dropna(thresh=2)) # eşik verebilirim.
print("\n \n",df)

df.fillna(value='DOLU')
print("\n \n",df.fillna(value='DOLU')) 
print("\n \n",df)

df['A'].fillna(value=df['A'].mean()) # ortalama
print("\n \n",df['A'].fillna(value=df['A'].mean())) 
print("\n \n",df)

print("-------------------------------------------------------------------------------------------------------")
print("\n \nGroupby")

data = {'Şirket': ['TURKCELL', 'TURKCELL', 'VODAFONE', 'VODAFONE', 'TTELEKOM', 'TTELEKOM'],
       'Kişi': ['Mehmet', 'Büşra', 'Selim', 'Caner', 'Gamze', 'Merve'],
       'Satış': [250, 325, 152, 645, 468, 525]}

df = pd.DataFrame(data)
print(df)

# SQL deki gibi
sirket = df.groupby('Şirket')
print("\n \n", df.dtypes)
print("\n \n HAFIZA:", sirket) # Hafızada nerede saklandığını gösteriyor.
print("\n \n", sirket['Satış'].mean())  # gruplara göre ortalama alır


sirket = df.groupby('Şirket')
print("\n \n SUM: ", sirket['Satış'].sum()) 

sirket = df.groupby('Şirket')
print("\n \n ", sirket['Satış'].std()) 

sirket = df.groupby('Şirket')
print("\n \n TURKCELL SUM:", sirket['Satış'].sum().loc['TURKCELL']) 


print("\n \n ", df.groupby('Şirket').max())

print("\n \n ", df.groupby('Şirket').describe()) # toplu bilgi 





