//Array Oluşturma:
//1
let meyveler = ["Elma", "Muz", "Çilek"];
console.log(meyveler);  // ["Elma", "Muz", "Çilek"]

//2
let sayilar = new Array(1, 2, 3, 4, 5);
console.log(sayilar);  






let indeks = sayilar.indexOf(5); //indexOf(): Belirtilen elemanın dizideki indeksini döner.
console.log(indeks);  

let varMi = sayilar.includes(30);
console.log(varMi);  // true (30 dizide var)

sayilar.reverse();
console.log(sayilar); 





for (let i = 0; i < meyveler.length; i++) {
    console.log(meyveler[i]);
}


meyveler.forEach(function(meyve) {
    console.log(meyve);
});


let matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

console.log(matris[0][1]);  // 2 (0. dizinin 1. indeksi)

// Ürünler, fiyatlar ve renkler için üç ayrı dizi
let urunler = ["iphone 12", "iphone 13", "iphone 13 pro"];
let fiyatlar = [9000, 12000, 20000];
let renkler = ["gold", "siyah", "beyaz"];

// Ürün 1, dizi şeklinde tanımlandı
let urun1 = ["iphone 12", 9000, "gold"];

// Ürün 2, boş bir diziye elemanlar atandı
let urun2 = [];
urun2[0] = "iphone 13";
urun2[1] = 12000;
urun2[2] = "siyah";

// Ürün 3, çok boyutlu dizi şeklinde tanımlandı
let urun3 = [
  "iphone 13 pro",
  20000,
  ["siyah", "beyaz", "mavi"]
];

// Ürün 3'ün 2. indeksindeki rengi "mavi" olarak değiştirdik
urun3[2] = "mavi";

// Dizilerdeki elemanları konsola yazdırma
console.log(urunler[0]);  // "iphone 12"
console.log(urun3[2]);    // "mavi"
console.log(urun3[2][0]); // Hata: urun3[2] artık bir string, bu yüzden indekslenemez

// Çok boyutlu diziden belirli indeksleri kontrol etme (geçmiş versiyonda çalışıyorsa)
console.log(urun3[2][1]);  // "beyaz"
console.log(typeof urun3[2]);  // "string" çünkü urun3[2] artık bir string

// Template Literals ile ürün, fiyat ve renkleri birleştirerek yazdırma
console.log(`${urunler[0]} - ${fiyatlar[0]} - ${renkler[0]}`); // "iphone 12 - 9000 - gold"
console.log(`${urunler[1]} - ${fiyatlar[1]} - ${renkler[1]}`); // "iphone 13 - 12000 - siyah"
console.log(`${urunler[2]} - ${fiyatlar[2]} - ${renkler[2]}`); // "iphone 13 pro - 20000 - beyaz"

// Bir string üzerinde indeksleme
let kursAdi = "Komple Web Geliştirme Eğitimi";
console.log(kursAdi[5]);  // "e" (5. indeks karakteri)

// String'i boşluklardan bölüp belirli indeksteki kelimeyi almak
console.log(kursAdi.split(" ")[3]);  // "Eğitimi" (4. kelime)


// Öğrenciler dizisini tanımlıyoruz
let ogrenciler = ["çınar", "yiğit", "ada"];

// Dizi uzunluğunu alıyoruz
sonuc = ogrenciler.length;  
console.log("Dizideki Eleman Sayısı:", sonuc);  // 3 eleman var

// Diziyi string'e çevirme
sonuc = ogrenciler.toString();  // Diziyi string'e dönüştürür
console.log("Dizi String:", sonuc);  // "çınar,yiğit,ada"

sonuc = ogrenciler.join(" ");  // Diziyi boşlukla ayırarak string'e dönüştürür
console.log("Boşluk ile Birleştirilmiş String:", sonuc);  // "çınar yiğit ada"

// Eleman silme işlemleri
sonuc = ogrenciler.pop();  // Son elemanı siler ve geri döndürür
console.log("Pop Sonucu (son eleman silinir):", sonuc);  // "ada"
console.log("Pop sonrası Dizi:", ogrenciler);  // ["çınar", "yiğit"]

sonuc = ogrenciler.shift();  // İlk elemanı siler ve geri döndürür
console.log("Shift Sonucu (ilk eleman silinir):", sonuc);  // "çınar"
console.log("Shift sonrası Dizi:", ogrenciler);  // ["yiğit"]

// Eleman ekleme işlemleri
sonuc = ogrenciler.push("sena");  // Diziye sonuna yeni eleman ekler
console.log("Push sonrası Dizi:", ogrenciler);  // ["yiğit", "sena"]

sonuc = ogrenciler.unshift("sena");  // Diziye başına yeni eleman ekler
console.log("Unshift sonrası Dizi:", ogrenciler);  // ["sena", "yiğit", "sena"]

// Marka dizileri oluşturuyoruz
let markalar1 = ["mazda", "toyota"];
let markalar2 = ["opel", "renault"];
let markalar3 = ["mercedes"];

// Dizileri birleştirme (concat)
sonuc = markalar1.concat(markalar2, markalar3);
console.log("Birleştirilmiş Dizi:", sonuc);  // ["mazda", "toyota", "opel", "renault", "mercedes"]

// Eleman silme ve ekleme (splice)
sonuc = markalar1.splice(0, 1, "bmw", "audi");  // 0. indeksten 1 eleman sil ve yerine "bmw", "audi" ekle
console.log("Splice Sonucu (silinen eleman):", sonuc);  // ["mazda"] (ilk eleman silindi)
console.log("Splice sonrası Dizi:", markalar1);  // ["bmw", "audi", "toyota"]

// Sadece eleman silme (splice)
sonuc = markalar1.splice(0, 1);  // 0. indeksten 1 eleman sil
console.log("Sadece Silinen Eleman:", sonuc);  // ["bmw"]
console.log("Silme sonrası Dizi:", markalar1);  // ["audi", "toyota"]
