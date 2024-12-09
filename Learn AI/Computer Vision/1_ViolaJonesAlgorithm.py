"""
- yüz tanıma gibi görsel tanıma problemleri için geliştirilmiş bir algoritmadır. (2001 yılında Paul Viola ve Michael Jones )
- makine öğrenimi (ML) algoritmalarından denetimli öğrenme yaklaşımına dayanır
- Adaboost gibi bir makine öğrenimi tekniği kullanır ve etiketli verilerle eğitilerek bir sınıflandırıcı oluşturur.
- Sağ ve slda sorun yaşıyor. Önden görünecek yüz.
---1. Haar3. Cascade Classifier (Kaskad Sınıflandırıcı): Özellikleri (Haar Features): bir görüntüdeki kontrast farklarını vurgular ve belirli yüz
 özelliklerini (gözler, burun, ağız) tanımaya yardımcı olur. 
---2. Adaboost (Adaptive Boosting): Adaboost’un avantajı, doğru sınıflandırıcıları (yüz tanıma için) hızla geliştirmesi ve düşük hesaplama maliyeti
 ile doğru sonuçlar elde etmesidir.
---3. Cascade Classifier (Kaskad Sınıflandırıcı): yüzleri tanıma işlemini çok aşamalı (kaskad) bir yapıda yapar. İlk aşama hızlı bir şekilde
"yüz mü, değil mi?" sorusuna yanıt verir. Eğer bu aşamadan geçerse, bir sonraki aşamaya geçirilir ve daha ayrıntılı özellikler incelenir.

Viola-Jones algoritması, yüksek doğruluk oranıyla hızlı yüz tanıma sağlayan, Haar özellikleri, Adaboost ve kaskad sınıflandırıcılar kullanarak 
çalışan bir yöntemdir. Bu algoritma, özellikle gerçek zamanlı uygulamalarda yaygın olarak kullanılır ve video akışlarında yüz tespiti gibi görevlerde
oldukça etkilidir.
"""

"""
Viola-Jones algoritması
   /      \
  /        \
1)Eğitim   2)Tanıma

Eğitim:

-resim 24px e 24px küçültülür
-özellikler aranır. hangi özellik yaygın resimde karar verir 180.000 özellik -->Adaboost ile çözülür [TOPLULUK] --> hata yapılana ağırlık verilir
-Çok resim gerekiyor
-Cascading (dizisel sıralama), çok sayıda sınıflandırıcıyı (classifier) bir arada kullanarak, her adımda "olmaz" kararlarını hızlı bir şekilde eleyip, 
sadece doğruya yakın sonuçları bir sonraki aşamaya taşımayı amaçlayan bir tekniktir. Bu, işlem süresini önemli ölçüde hızlandırır ve yanlış pozitifleri
(false positives) azaltır.

Tanıma:

-Siyah beyaz yap resim 
-yüz arar, adım adım kayarak kare ile, göz ve kaş aramak gibi
- iki göz bir burun bir ağız bulduğu karede işaretliyor. Ama resmi gezmeye devam ediyor
-kare büyüklüğü değişitirerek büyütrek hep tarar. 

Haar-like özellikler:
-Kenar Özellikler beyaz karanlık  (Alın kaş) Burunda falan genelde olur
---Sonra piksel piksel bakılır. Değer verilir. 0 ve 1 arasında, karanlık 1 e yakın.
--- aydınlık kısmın ortalaması alınır. karanlık kısmın alınır ortalaması
---Siyah - Beyaz  çıkarılır. İdeal senaryoda bu rakam 1 dir. 1 e ne kadar yakınsa aradığımız senaryoya o kadar yakınız. Eşik değerler var bunu biz belirleriz
-Çizgi Özellikler beyaz karanlık beyaz (dudak içi karanlık dudak.) göz falan genelde
-Dört kare Özellikler 

Integral Resmi: daha hızlı boyutu büyük olsada 

  
"""
#ses ayırma --> audio remover
