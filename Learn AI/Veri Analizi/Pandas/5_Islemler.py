import numpy as np
import pandas as pd

df = pd.DataFrame({'col1': [1,2,3,4],
                   'col2': [444,555,666,444],
                   'col3': ['abc','def','ghi','xyz']})

print(df['col2'].unique()) # benzersiz olan sütunları döndürür

print(df['col2'].nunique()) # kaç benzersiz var

print(df['col2'].value_counts()) # hangi değerden kaç tane var

def carpi2(x):
    return x*2
print(df['col1'].apply(carpi2)) # apply ile fonk. kullanabiliyorum

print(df['col3'].apply(len)) # pythonnun içindeki fonk. ları da kullanabilirsin

print(df['col2'].apply(lambda x: x*2))

print(df.columns)

print(df.index)

print(df.sort_values('col2'))

print(df.isnull())

data = {'A':['G1','G1','G1','G2','G2','G2'],
        'B':['bir','bir','iki','iki','bir','bir'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)
print(df)
print(df.pivot_table(values='D', index=['A', 'B'], columns=['C'])) # çoklu indexli bir dataframe
