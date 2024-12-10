from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

# WebDriver Manager ile ChromeDriver'ı otomatik olarak indir ve kullan
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Trendyol'da doğal bal arama sayfasına git
driver.get("https://www.trendyol.com/sr?q=do%C4%9Fal+bal+&qt=do%C4%9Fal+bal+&st=do%C4%9Fal+bal+&os=1&pi=1")

# Sayfanın tamamen yüklenmesini bekle
time.sleep(5)

# Sayfayı aşağı kaydırarak tüm ürünlerin yüklenmesini sağlaaa
SCROLL_PAUSE_TIME = 5
MAX_SCROLLS = 100  # En fazla kaç kez kaydırma yapılacağını belirle

product_links = []
max_product_count = 100  # Çekilecek maksimum ürün sayısı
scroll_count = 0

# Sayfanın başlangıçta yüklendiğinden emin olmak için bir süre bekleyelim
time.sleep(5)

while len(product_links) < max_product_count and scroll_count < MAX_SCROLLS:
    # Sayfayı aşağı kaydır (adım adım kaydırma)
    driver.execute_script("window.scrollBy(0, 400);")

    # Yeni verilerin yüklenmesini bekle
    time.sleep(SCROLL_PAUSE_TIME)

    # Yeni ürün linklerini topla
    products = driver.find_elements(By.CLASS_NAME, 'p-card-wrppr')
    for product in products:
        if len(product_links) >= max_product_count:
            break
        try:
            # Ürün linkini bul ve listeye ekle
            link = product.find_element(By.TAG_NAME, 'a').get_attribute('href')
            if link not in product_links:
                product_links.append(link)
        except Exception as e:
            print(f"Link çekme hatası: {e}")

    # Scroll sayısını artır
    scroll_count += 1

# Çekilen verileri kaydetmek için bir liste oluştur
data = []

# Her ürün için id eklemek için sayaç
product_id = 1

# Tüm ürün linklerinde dolaş
for link in product_links:
    try:
        # Ürün sayfasına git
        driver.get(link)
        
        # Sayfanın yüklenmesini bekle
        time.sleep(3)

        # Ürün başlığını çek
        try:
            title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'pr-new-br'))
            ).text
        except:
            title = "Başlık Bulunamadı"
        
        # Ürün fiyatını çek
        try:
            price = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'prc-dsc'))
            ).text
        except:
            price = "Fiyat Bulunamadı"
        
        # Ürün açıklamasını çek
        try:
            description = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.pr-in-cn'))
            ).text
        except:
            description = "Açıklama Bulunamadı"
        
        # Ürün bilgilerini JSON formatında yapıya ekle
        product_data = {
            "id": product_id,
            "Ürün Başlığı": title,
            "Fiyat": price,
            "Açıklama": description
        }
        
        data.append(product_data)
        
        # Bilgileri ekrana yazdır
        print(f"Ürün ID: {product_id}\nÜrün: {title}\nFiyat: {price}\nAçıklama: {description}\n{'-'*30}")
        
        # Ürün id'yi artır
        product_id += 1

        # Biraz bekle
        time.sleep(2)
        
    except Exception as e:
        print(f"Veri çekme hatası: {e}")

# Verileri JSON dosyasına kaydet
with open('urun_detaylari.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Tüm veriler JSON dosyasına kaydedildi.")

# Tarayıcıyı kapat
driver.quit()
