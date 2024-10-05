let sonuc;

// Farklı veri tiplerine dönüştürme işlemleri
sonuc = 10;                    // Sayı türünde bir değer
sonuc = "10";                  // String türünde bir değer
sonuc = Number("10");          // String'i sayıya çevirir
sonuc = parseInt("10.6");      // String'i tam sayıya çevirir (ondalıklı kısmı atar)
sonuc = parseFloat("10.6");    // String'i ondalıklı sayıya çevirir
sonuc = parseInt("10a");       // String'ten ilk sayısal kısmı alır, "10" olarak döner
sonuc = parseInt("a10");       // Harflerle başladığı için NaN döner

// NaN kontrolü
sonuc = isNaN("10");           // "10" sayıya dönüştürülebilir olduğu için false döner

// Ondalık sayılarla işlemler
let sayi = 15.12355667;

sonuc = sayi.toPrecision(5);   // Toplam 5 basamaklı yuvarlanmış bir sayı döner
sonuc = sayi.toFixed(5);       // Ondalık kısmı 5 basamağa yuvarlanmış bir sayı döner

console.log(typeof sonuc);     // Sonucun veri tipini gösterir
console.log(sonuc);            // Sonucu konsola yazdırır

// Matematiksel işlemler (Math nesnesi ile)
sonuc = Math.round(2.4);       // Yakın en yakın tam sayıya yuvarlar (2)
sonuc = Math.round(2.6);       // Yakın en yakın tam sayıya yuvarlar (3)
sonuc = Math.ceil(2.2);        // Yukarı yuvarlar (3)
sonuc = Math.floor(2.6);       // Aşağı yuvarlar (2)
sonuc = Math.sqrt(25);         // Karekökünü alır (5)
sonuc = Math.pow(2, 3);        // 2'nin 3. kuvvetini alır (8)
sonuc = Math.abs(-10);         // Mutlak değerini alır (10)
sonuc = Math.min(4, 6, 8, 3, 9);  // Verilen sayıların en küçüğünü bulur (3)
sonuc = Math.max(4, 6, 8, 3, 9);  // Verilen sayıların en büyüğünü bulur (9)
sonuc = Math.floor(Math.random() * 100) + 50;  // 50 ile 150 arasında rastgele bir tam sayı üretir

console.log(typeof sonuc);     // Sonucun veri tipini gösterir
console.log(sonuc);            // Sonucu konsola yazdırır


