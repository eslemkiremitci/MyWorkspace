from PIL import Image, ImageEnhance

# Görüntüyü Yükleme
image_path = r"C:\Users\eslem\OneDrive\Masaüstü\MyWorkspace\Image quality enhancement\New folder\image.png"
img = Image.open(image_path)

# Görüntüyü RGB moduna dönüştürme (JPEG kaydedebilmek için)
if img.mode == 'RGBA':
    img = img.convert('RGB')

# Keskinlik ve Kontrast Artırma
enhancer = ImageEnhance.Sharpness(img)
img = enhancer.enhance(2.0)  # Keskinlik artırma

enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(1.5)  # Kontrast artırma

# Sonuç: Görüntüyü Kaydetme
img.save(r"C:\Users\eslem\OneDrive\Masaüstü\MyWorkspace\Image quality enhancement\New folder\iyilestirilmis_fotograf.jpg")
img.show()
