import os
import subprocess

def convert_and_clean_folder(folder_path, output_quality=2):
    """
    Bir klasördeki tüm ses dosyalarını MP3 formatına dönüştür ve orijinal dosyaları sil.
    
    :param folder_path: Dönüştürülecek dosyaların bulunduğu klasör.
    :param output_quality: MP3 kalite ayarı (0-9 arası; 0 en yüksek kalite, 9 en düşük kalite).
    """
    try:
        files = os.listdir(folder_path)
        
        for file in files:
            input_file = os.path.join(folder_path, file)
            
            # Sadece ses/video dosyalarını işleme al (ör. .webm, .wav, .flac, .m4a)
            if os.path.isfile(input_file) and not file.endswith(".mp3"):
                output_file = os.path.splitext(input_file)[0] + ".mp3"
                
                try:
                    # FFmpeg ile dönüştürme işlemi (otomatik üzerine yazma için -y ekli)
                    command = [
                        "ffmpeg", "-y", "-i", input_file,
                        "-codec:a", "libmp3lame",
                        "-qscale:a", str(output_quality),
                        output_file
                    ]
                    print(f"Dönüştürülüyor: {file} → {os.path.basename(output_file)}")
                    subprocess.run(command, check=True)

                    # Eğer dönüştürme başarılı olduysa orijinal dosyayı sil
                    if os.path.exists(output_file):
                        os.remove(input_file)
                        print(f"Orijinal dosya silindi: {file}")
                
                except subprocess.CalledProcessError as e:
                    print(f"Hata oluştu: {file} dönüştürülemedi. {e}")
    
        print("Tüm dosyalar başarıyla dönüştürüldü ve orijinal dosyalar silindi.")
    
    except Exception as e:
        print(f"Genel bir hata oluştu: {e}")

# Kullanım
input_folder = r"C:\Users\eslem\OneDrive\Masaüstü\pop"  # Klasör yolunu güncelleyin
convert_and_clean_folder(input_folder)
