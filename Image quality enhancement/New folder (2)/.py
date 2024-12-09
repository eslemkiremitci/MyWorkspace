from rembg import remove
from PIL import Image, ImageEnhance, ImageFilter
import io
import numpy as np

# Girdi ve çıktı dosya yollarını tanımlayın
input_image_path = r'C:\New folder (2)\1.jpg'  # Arka planını temizlemek istediğiniz logonun yolu
output_image_path = r'C:\New folder (2)\2.png'  # Temizlenmiş logonun kaydedileceği yol

# Görüntüyü yükle
input_image = Image.open(input_image_path).convert("RGBA")  # RGBA formatına dönüştür

# 1. Ön İşleme: Görüntüyü iyileştirme
# Parlaklık ve kontrast artırma
enhancer = ImageEnhance.Contrast(input_image)
image_enhanced = enhancer.enhance(1.2)  # Kontrastı hafifçe artır
image_enhanced = ImageEnhance.Brightness(image_enhanced).enhance(1.1)  # Parlaklığı hafifçe artır

# Görüntüyü BytesIO formatına dönüştür
input_image_bytes = io.BytesIO()
image_enhanced.save(input_image_bytes, format='PNG')
input_image_bytes = input_image_bytes.getvalue()

# 2. rembg ile arka planı temizleme
output_image_bytes = remove(input_image_bytes)

# Çıktıyı yeniden yükle
output_image = Image.open(io.BytesIO(output_image_bytes)).convert("RGBA")

# 3. Son İşleme: Kenarları yumuşatma ve renklerin korunması
# Orijinal görüntü ile rembg sonucunu birleştir
output_array = np.array(output_image)
original_array = np.array(input_image)

# Şeffaflık maskesini iyileştir
alpha_channel = output_array[:, :, 3]  # Alpha kanalı
smooth_alpha = Image.fromarray(alpha_channel).filter(ImageFilter.GaussianBlur(radius=2))  # Gaussian Blur ile yumuşatma
smooth_alpha = np.array(smooth_alpha)

# Orijinal renkleri geri kazandırma
output_array[:, :, :3] = np.where(smooth_alpha[:, :, None] > 50, original_array[:, :, :3], output_array[:, :, :3])

# Yumuşatılmış alpha kanalını yeniden uygula
output_array[:, :, 3] = smooth_alpha

# Son görüntüyü oluştur
final_image = Image.fromarray(output_array, "RGBA")

# Çıktıyı kaydet
final_image.save(output_image_path)

print(f"Arka plan temizlenmiş ve renkleri korunmuş logo kaydedildi: {output_image_path}")
