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



