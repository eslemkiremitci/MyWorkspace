import yt_dlp
import os
from pydub import AudioSegment

# Playlist'teki videoları indir
def download_playlist(playlist_url, download_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'noplaylist': False,  # Tüm playlisti indir
        'ignoreerrors': True,  # Hatalı videoları atla
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

    return [f for f in os.listdir(download_path) if f.endswith('.webm') or f.endswith('.m4a')]

# MP3 formatına dönüştür
def convert_to_mp3(video_files, download_path):
    for video_file in video_files:
        video_path = os.path.join(download_path, video_file)
        mp3_path = os.path.splitext(video_path)[0] + ".mp3"
        
        audio = AudioSegment.from_file(video_path)
        audio.export(mp3_path, format="mp3")
        
        print(f"Dönüştürme tamamlandı: {mp3_path}")
        os.remove(video_path)  # İndirilen video dosyasını sil

if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/watch?v=G81e4utp3Mo"  # Playlist URL'si
    download_path = "./"  # İndirilecek dosya yolu

    # Playlist'teki videoları indir ve MP3'e dönüştür
    video_files = download_playlist(playlist_url, download_path)
    convert_to_mp3(video_files, download_path)
    print("Tüm videolar MP3 formatına dönüştürüldü.")
