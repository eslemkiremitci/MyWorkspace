let ad = "SHüseyin";
let soyad = "Kiremitci";
let yas = 63;
let sehir = "Konya";

let mesaj = "Benim adım " + ad + " ve soyadım " + soyad + ". " + sehir + "'de yaşıyorum." + "Emekliliğe " + (65 - yas) + " yılım kaldı.";

// backtick (Template Literals ile daha kısa yazım)
mesaj = `Benim adım ${ad} ve soyadım ${soyad}. ${sehir}'de yaşıyorum. Emekliliğe ${65 - yas} yılım kaldı.`;

// ternary operators (Koşul operatörü)
let emeklilik = (65 - yas > 0) ? "Emekliliğe " + (65 - yas) + " yıl kaldı." : "Zaten emekli oldunuz.";

console.log(mesaj);


// Tek tırnak işareti (Single Quote) kullanımı
let text1 = 'It\'s alright.';  // Tek tırnak işaretini kaçış karakteri (\) ile ekledik
console.log(text1);  // Çıktı: It's alright.

// Çift tırnak işareti (Double Quote) kullanımı
let text2 = "We are the so-called \"Vikings\" from the north.";  // Çift tırnak için kaçış karakteri kullandık
console.log(text2);  // Çıktı: We are the so-called "Vikings" from the north.

// Ters eğik çizgi (Backslash) kullanımı
let text3 = "The character \\ is called backslash.";  // Bir ters eğik çizgi eklemek için çift backslash (\) kullanıyoruz
console.log(text3);  // Çıktı: The character \ is called backslash.

// Özet: JavaScript'te kaçış karakterleri, özel karakterlerin string içinde doğru bir şekilde gösterilmesi için kullanılır.
// Örneğin, tek tırnak, çift tırnak veya ters eğik çizgi gibi karakterleri eklemek için backslash (\) kullanılır.








let kursAdi = "Komple Uygulamalı Web Geliştirme Eğitimi."; // Orijinal string
let sonuc; // Sonuçları tutmak için bir değişken

// 1. toLowerCase() - Tüm harfleri küçük harfe çevirir
sonuc = kursAdi.toLowerCase();
console.log(sonuc); // "komple uygulamalı web geliştirme eğitimi."

// 2. toUpperCase() - Tüm harfleri büyük harfe çevirir
sonuc = kursAdi.toUpperCase();
console.log(sonuc); // "KOMPLE UYGULAMALI WEB GELİŞTİRME EĞİTİMİ."

// 3. length - String'in uzunluğunu verir
sonuc = kursAdi.length;
console.log(sonuc); // 40 (karakter sayısı)

// 4. [1] - String'in belirli bir indeksindeki karakteri döner (0'dan başlar)
sonuc = kursAdi[1];
console.log(sonuc); // "o" (1. indeks karakteri)

// 5. slice(başlangıç, bitiş) - Belirli bir aralıktaki karakterleri alır (bitiş dahil değil)
sonuc = kursAdi.slice(0, 6);
console.log(sonuc); // "Komple"

// 6. slice(başlangıç) - Başlangıçtan itibaren keser
sonuc = kursAdi.slice(10);
console.log(sonuc); // "Web Geliştirme Eğitimi."

// 7. slice(-10) - Negatif indeks kullanarak sondan keser
sonuc = kursAdi.slice(-10);
console.log(sonuc); // "Eğitimi."

// 8. slice(-10, -5) - Sondan başlayarak belirli bir aralığı keser
sonuc = kursAdi.slice(-10, -5);
console.log(sonuc); // "Eğiti"

// 9. substring(başlangıç, bitiş) - slice gibi çalışır ama negatif indeks kullanmaz
sonuc = kursAdi.substring(0, 6);
console.log(sonuc); // "Komple"

// 10. substring(başlangıç) - Başlangıçtan itibaren keser
sonuc = kursAdi.substring(10);
console.log(sonuc); // "Web Geliştirme Eğitimi."

// 11. replace(eski, yeni) - Belirtilen bir string'i yenisi ile değiştirir
sonuc = kursAdi.replace("Eğitimi", "Kursu");
console.log(sonuc); // "Komple Uygulamalı Web Geliştirme Kursu."

// 12. trim() - String'in başındaki ve sonundaki boşlukları kaldırır
sonuc = kursAdi.trim();
console.log(sonuc); // "Komple Uygulamalı Web Geliştirme Eğitimi." (boşluklar varsa kaldırılır)

// 13. trimEnd() - String'in sonundaki boşlukları kaldırır
sonuc = kursAdi.trimEnd();
console.log(sonuc); // Aynı trim() gibi, sonundaki boşlukları temizler

// 14. trimStart() - String'in başındaki boşlukları kaldırır
sonuc = kursAdi.trimStart();
console.log(sonuc); // Başındaki boşlukları temizler

// 15. indexOf("kelime") - Belirtilen kelimenin ilk geçtiği indeks değerini döner
sonuc = kursAdi.indexOf("Komple");
console.log(sonuc); // 0 (Komple, string'in başında)

// 16. split(" ") - String'i belirtilen karaktere göre böler ve bir dizi döner
sonuc = kursAdi.split(" ")[0];
console.log(sonuc); // ["Komple", "Uygulamalı", "Web", "Geliştirme", "Eğitimi."]
