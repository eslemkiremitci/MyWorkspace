import cairosvg

# Giriş ve çıkış dosyalarının adlarını belirtin
input_file = "1.png"  # PNG dosyanızın adı
output_file = "output_image.svg"  # Oluşturulacak SVG dosyasının adı

try:
    # PNG'yi SVG'ye dönüştür
    cairosvg.png2svg(url=input_file, write_to=output_file)
    print(f"Dönüştürme başarılı! SVG dosyası: {output_file}")
except Exception as e:
    print(f"Dönüştürme sırasında hata oluştu: {e}")
