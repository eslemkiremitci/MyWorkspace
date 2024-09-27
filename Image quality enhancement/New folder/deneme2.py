from rembg import remove
from PIL import Image, ImageEnhance, ImageFilter

def kalite_artirma(image_path, output_path):
    # Görüntüyü Yükleme
    img = Image.open(image_path)
    
    # Görüntüyü RGB Moduna Dönüştürme (Gerekli)
    img = img.convert("RGB")
    
    # Keskinlik ve Kontrast Artırma
    img = img.filter(ImageFilter.SHARPEN)  # Keskinlik artırma
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)  # Kontrast artırma

    # Sonuç Görüntüsünü Kaydetme
    img.save(output_path)
    print(f"Kalite artırılmış görüntü kaydedildi: {output_path}")
    return img

def arka_plan_temizleme(input_image):
    # Arka Planı Kaldırma
    output_image = remove(input_image)
    return output_image

def arka_plan_ekleme(product_image, background_image_path, output_path, position=(100, 100), size=(500, 500)):
    # Arka Plan ve Ürün Görsellerini Yükleme
    background = Image.open(background_image_path)

    # Ürünün Boyutunu Ayarlama
    product_image = product_image.resize(size)

    # Ürünü Arka Planın Üzerine Yapıştırma
    background.paste(product_image, position, product_image)  # Ürünü arka planın istediğiniz kısmına yapıştırın

    # Eğer arka plan RGBA modundaysa, RGB moduna dönüştür
    if background.mode == 'RGBA':
        background = background.convert('RGB')

    # Sonuç Görselini Kaydetme ve Gösterme
    background.save(output_path)
    print(f"Birleştirilmiş görüntü kaydedildi: {output_path}")
    background.show()

def main():
    # Orijinal Fotoğraf Yolu
    original_image_path = 'C:/Users/eslem/OneDrive/Masaüstü/MyWorkspace/Image quality enhancement/New folder/kitap.png'  # Ürün fotoğrafı yolunu buraya yazın

    # Kalite Artırma
    kalite_artirilmis_yol = 'C:/Users/eslem/OneDrive/Masaüstü/MyWorkspace/Image quality enhancement/New folder/iyilestirilmis_fotograf2.jpg'
    iyilestirilmis_gorsel = kalite_artirma(original_image_path, kalite_artirilmis_yol)

    # Arka Plan Temizleme
    arka_plansiz_gorsel = arka_plan_temizleme(iyilestirilmis_gorsel)
    arka_plansiz_yol = 'C:/Users/eslem/OneDrive/Masaüstü/MyWorkspace/Image quality enhancement/New folder/arka_plansiz_fotograf.png'
    arka_plansiz_gorsel.save(arka_plansiz_yol)
    print(f"Arka plansız görüntü kaydedildi: {arka_plansiz_yol}")

    # Ürün ile Uyumlu Arka Plan Görseli
    arka_plan_yolu = 'C:/Users/eslem/OneDrive/Masaüstü/MyWorkspace/Image quality enhancement/New folder/arka_plan.png'  # Ürün ile uyumlu arka plan görselinin yolunu buraya yazın
    birlesik_yol = 'C:/Users/eslem/OneDrive/Masaüstü/MyWorkspace/Image quality enhancement/New folder/birlesik_fotograf.jpg'
    
    # Arka Plan Ekleyerek Görseli Birleştirme
    try:
        arka_plan_ekleme(arka_plansiz_gorsel, arka_plan_yolu, birlesik_yol, position=(100, 100), size=(500, 500))
    except FileNotFoundError:
        print(f"Dosya bulunamadı: {arka_plan_yolu}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == '__main__':
    main()
