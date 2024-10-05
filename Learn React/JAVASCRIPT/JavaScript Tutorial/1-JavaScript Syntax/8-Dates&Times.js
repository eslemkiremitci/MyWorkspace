// Şu anki tarih ve saati almak için Date nesnesi kullanıyoruz
let simdi = new Date();  // Şu anki tarih ve saat

// Get Methods (Tarih ve saat bilgilerini al)
sonuc = simdi.getDate();        // Gün bilgisini alır
console.log("Gün:", sonuc);     // Örnek çıktı: 13

sonuc = simdi.getDay();         // Haftanın gününü alır (0: Pazar, 6: Cumartesi)
console.log("Haftanın günü:", sonuc); // Örnek çıktı: 4 (Perşembe)

sonuc = simdi.getFullYear();    // Yıl bilgisini alır
console.log("Yıl:", sonuc);     // Örnek çıktı: 2024

sonuc = simdi.getHours();       // Saat bilgisini alır
console.log("Saat:", sonuc);    // Örnek çıktı: 15

sonuc = simdi.getTime();        // 1 Ocak 1970'ten bu yana geçen milisaniye sayısını alır
console.log("Zaman (milisaniye):", sonuc); // Örnek çıktı: 1700000000000

// Set Methods (Tarih ve saat bilgilerini değiştir)
simdi.setFullYear(2025);        // Yılı 2025 olarak ayarla
simdi.setMonth(7);              // Ayı Ağustos olarak ayarla (0: Ocak, 11: Aralık)
simdi.setDate(15);              // Günü 15 olarak ayarla

sonuc = simdi;
console.log("Yeni Tarih:", sonuc);  // Ayarlanmış yeni tarih: 15 Ağustos 2025

// Doğum tarihini Date nesnesi ile ayarla
let dogumTarihi = new Date(1990, 5, 15);  // 15 Haziran 1990 (Ay 0 tabanlı: 5 = Haziran)
console.log("Doğum Tarihi:", dogumTarihi);

// Doğum yılından bu yana geçen yıl sayısını hesapla
sonuc = simdi.getFullYear() - dogumTarihi.getFullYear();  // Şu anki yıl - doğum yılı
console.log("Yaş:", sonuc);  // Örnek çıktı: 35 (2025 - 1990)

// Doğum tarihinden bu yana geçen milisaniye sayısı
let milisecond = simdi - dogumTarihi;  // İki tarih arasındaki fark milisaniye cinsinden
console.log("Geçen milisaniye:", milisecond);

// Milisaniyeyi saniyeye çevir
let saniye = milisecond / 1000;  // Milisaniyeyi saniyeye çevirmek için 1000'e böleriz
console.log("Geçen saniye:", saniye);

// Saniyeyi dakikaya çevir
let dakika = saniye / 60;  // Saniyeyi dakikaya çevirmek için 60'a böleriz
console.log("Geçen dakika:", dakika);

// Dakikayı saate çevir
let saat = dakika / 60;  // Dakikayı saate çevirmek için 60'a böleriz
console.log("Geçen saat:", saat);

// Sonuçları yazdır
sonuc = dakika;
console.log("Dakika:", sonuc);
console.log("Sonucun Türü:", typeof sonuc);
