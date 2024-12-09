import cv2
import imageio
import imageio_ffmpeg

print(imageio_ffmpeg.get_ffmpeg_version())

face_cascade = cv2.CascadeClassifier(r'C:\MyWorkspace\Learn AI\Computer Vision\Face Detection\haarcascade-frontalface-default.xml')
eye_cascade = cv2.CascadeClassifier(r'C:\MyWorkspace\Learn AI\Computer Vision\Face Detection\haarcascade-eye.xml')

# bunlar cascade yüklemeleri


# video içinde tek bir resim karesine frame deniyor
# video genelde saniyede 25 ya da 30 frame olur buna FPS (Frames Per Second)
def detect(frame): # frame --> resim saniyede genelde
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # siyah beyaz yapma
    faces = face_cascade.detectMultiScale(gray, 1.1, 5) 
    # gray: Gri tonlamalı görüntüyü ifade eder.
    # scaleFactor (1.1): görüntünün her aramada ne kadar küçültüleceğini belirtir. 1.1 değeri, görüntüyü her adımda %10 oranında küçültmek anlamına gelir. Daha düşük bir değer, daha hassas bir arama sağlar
    # minNeighbors (5): Yani, bir yüz algılandıktan sonra çevresindeki "komşu dikdörtgenlerin" sayısını kontrol eder. Daha yüksek bir değer (6 veya 7 gibi), algılamayı daha katı hale getirir ve yanlış pozitifleri azaltır, ancak bazı yüzler atlanabilir.
    """
    minSize ve maxSize (Opsiyonel):

    minSize: Algılanan yüzlerin en küçük boyutunu belirler. Örneğin (30, 30) şeklinde bir değer verilirse, yalnızca 30x30 pikselden büyük yüzler algılanır.
    maxSize: Algılanan yüzlerin en büyük boyutunu belirler. Örneğin (300, 300) verilirse, yalnızca 300x300 pikselden küçük yüzler algılanır.
    Eğer belirtilmezse, bu parametreler varsayılan olarak boş bırakılır ve tüm boyutlarda yüzler aranır.
    """
    # for her yüz için 
    for (x, y, w, h) in faces:  # h boy, w yatay uzunluk, (x,y) -> dikdörtgenin  sol yukarı köşesi
        # dikdörtgen çizdirme
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5) # (x+w, y+h) sağ alt kordinat , (255, 0, 0) renk -> kırmızı, 5 dikdörtgen kalınlığı
        gray_face = gray[y:y + h, x:x + w]
        color_face = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(gray_face, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(color_face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    return frame

#YÜZ VE GÖZ BULUNDU ŞİMDİ VİDEOYA UYGULUYORUM.

reader = imageio.get_reader(r'C:\MyWorkspace\Learn AI\Computer Vision\Face Detection\1.mp4') 
fps = reader.get_meta_data()['fps']
writer = imageio.get_writer(r'C:\MyWorkspace\Learn AI\Computer Vision\Face Detection\output.mp4', fps=fps)
for i, frame in enumerate(reader):
    frame = detect(frame)
    writer.append_data(frame)
    print(i)
writer.close()
