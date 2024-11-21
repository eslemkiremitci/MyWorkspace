import pandas as pd
import pandas as pd
from sqlalchemy import create_engine

print("-----------------------CSV----------------------------")

df = pd.read_csv(r'C:\Users\eslem\OneDrive\Masaüstü\MyWorkspace\Learn AI\ML\Pandas\ornek.csv')

df.to_csv(r'C:\Users\eslem\OneDrive\Masaüstü\MyWorkspace\Learn AI\ML\Pandas\output.csv', index=False)

output_df = pd.read_csv(r'C:\Users\eslem\OneDrive\Masaüstü\MyWorkspace\Learn AI\ML\Pandas\output.csv')

print(pd.read_csv(r'C:\Users\eslem\OneDrive\Masaüstü\MyWorkspace\Learn AI\ML\Pandas\ornek.csv'))
print(output_df)

print("-----------------------Excel dosyasını okuma----------------------------")

print(pd.read_excel(r'C:\Users\eslem\OneDrive\Masaüstü\MyWorkspace\Learn AI\ML\Pandas\excel-ornek.xlsx', sheet_name='Sheet1'))

# 2. DataFrame'i yeni bir Excel dosyasına yazma
print(df.to_excel(r'C:\Users\eslem\OneDrive\Masaüstü\MyWorkspace\Learn AI\ML\Pandas\output2.xlsx', sheet_name='Yeni', index=False))
print("Excel dosyası başarıyla kaydedildi!")

print("-----------------------HTML Tablosunu Okuma----------------------------")
# 3. HTML tablosunu okuma
data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')

# 4. Veri türünü yazdırma
print(type(data))

# 5. İlk tabloyu yazdırma
print(data[0])

print("-----------------------SQLite Veritabanı Oluşturma----------------------------")

engine = create_engine('sqlite:///:memory:') # Hafızada bir SQLite veritabanı oluşturur. Veritabanıyla etkileşim için bir bağlantı (engine) oluşturulur.

print(df.to_sql('my_table', engine)) # DataFrame, SQLite veritabanında bir tablo olarak saklanır.

print(pd.read_sql('my_table', engine)) # Veritabanından Veri Okuma

print()

