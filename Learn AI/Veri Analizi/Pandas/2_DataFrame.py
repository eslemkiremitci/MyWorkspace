import numpy as np
import pandas as pd
"""
DataFrame, yapılandırılmış bir veri kümesini temsil eden iki boyutlu (2D) bir veri yapısıdır.
Tablolar şeklinde düşünebilirsin: satırlar ve sütun
Satırlar index ile numaralandırılır (varsayılan olarak 0'dan başlar).
Sütunlar ise birer isim alabilir (genellikle başlık veya değişken adı).
Aynı DataFrame içinde farklı veri türleri (örneğin, sayılar, metinler, tarihler) bulunabilir.
Veri manipülasyon işlemi için uygun fonksiyonlar sunar.
Bir DataFrame oluşturmak için genellikle bir Python sözlüğü (dictionary) veya bir dış veri kaynağı (CSV, Excel dosyası gibi) kullanılır.
"""

#np.random.seed(10)
#Aynı kod parçası çalıştırıldığında, aynı rastgele sayılar üretilir.
#Bir modeli test etmek veya bir algoritmanın çıktısını karşılaştırmak istediğinizde faydalıdır. Debugging (Hata Ayıklama) Faydalı
#Kodunuzu başkalarıyla paylaştığınızda, aynı sonuçları elde etmelerini sağlar.
np.random.seed(10) 
#Data - İndex (Satır * Sütun)
df = pd.DataFrame(np.random.randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])


print(df)
print(df['W']) #sütun alma
print(df[['W', 'Y']]) #sütunlar alma
print(type(df['W']))
df['yeni'] = df['W'] + df['Y'] #yeni sütunu ekler direk df. Datalarını atamak zorundasın. 
print("Yeniiiiii: \n",df['yeni'])
print(df)

#sütun
df.drop('yeni', axis=1, inplace=True) #sütun silmek için, ismi, sütun sil dedim, Ama bu kısma kadar DataFrame yansımaz. Yansısın diye inplace kullanılır. 
print(df)

#satır
print(df.drop('E'))#satırda axis vermeme gerek yok.
print(df) # dikkat kayıt etmedi


#Satır seçme:
print("------------------------------------------------ Satır Seçme ---------------------------------------------------------------")
print(df.loc['A'])
print(df.iloc[2]) #index ile de alabilirsin. Harfle verilmiş olsa bile
print("\nC satır, Z sütunu: ", df.loc['C', 'Z'])
print("\n", df.loc[['A', 'D'], ['X', 'Z']])

print("---------------------------------------------Koşullu seçim------------------------------------------------------------------")
booldf = df>0
print(df[booldf])
print("\n \n", df[df>0])
print("\n \n", df['W'] > 0)
print("\n \n", df[df['W']>0][['Y', 'Z']]) # df['W']>0 koşulu a b c satırını verdi. y ve z de sütunu
# and operatörü sadece boolean için kullanılabilir.
print("\n \n", df[(df['W']>0) & (df['Z']>1)]) #ikisinde doğru olduğu tek satırr varmış 
print("\n \n", df[(df['W']>0) | (df['Z']>1)])

print("\n \n", df.reset_index()) # index sütun oldu KALICI DEĞİL inplace=True KULLANMADIM 

sehir = 'Ankara İstanbul İzmir Bursa Adana'.split()
df['Şehir'] = sehir
print(df)

print(df.set_index('Şehir')) #yeni index oluşturma

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index_mul = pd.MultiIndex.from_tuples(hier_index)

print("\n \n", hier_index)
print("\n \n", hier_index_mul)

dff = pd.DataFrame(np.random.randn(6,2), hier_index_mul, ['A', 'B'])

print("\n \n",dff)

print("\n \n",dff.loc['G1'].loc[1])


dff.index.names = ['Grup', 'Sayı']
print("\n \n",dff)
print("\n \n",dff.loc['G1']) #loc, etiketlere göre satır veya sütun seçimi yapar.
print("\n \n",dff.xs('G1')) #xs (cross-section), MultiIndex veri yapılarında, tek bir seviye üzerinden kesit almak için kullanılır.
#Daha sade ve hızlı bir yöntemdir çünkü diğer seviyeleri otomatik olarak dışlar.
print(dff.xs(1, level='Sayı'))


