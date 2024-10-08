// 1. Function Declaration (Fonksiyon Bildirimi)
function selamVer() {
    console.log("Merhaba!");
  }
  
  selamVer();  // "Merhaba!" yazdırılır
  
  // 2. Function Expression (Fonksiyon İfadesi)
  let selamVer2 = function () {
    console.log("Merhabaaaa!");
  };
  
  selamVer2();  // "Merhabaaaa!" yazdırılır
  
  // 3. Arrow Function (Ok Fonksiyonu)
  // ES6 ile gelen bir fonksiyon tanımlama yöntemidir. Daha kısa ve sade bir syntax sağlar.
  let selamVer3 = () => {
    console.log("Merhabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!");
  };
  
  selamVer3();  // "Merhaba!" yazdırılır
  
  // 4. Parametre Alan Fonksiyon ve Arrow Function
  let toplaArrow = (a, b) => a + b;
  console.log(toplaArrow(5, 3));  // 8
  
  // Aynı isim çakışmalarını önlemek için toplaArrow ve topla isimlerini farklı tuttuk
  function topla(a, b) {
    return a + b;
  }
  
  let sonuc1 = topla(4, 7);
  console.log("Toplam:", sonuc1);  // 11
  

  function test() {
    return "İlk return";
    console.log("Bu satır çalışmaz.");  // Bu satır çalışmayacak çünkü return sonrasında.
  }
  
  console.log(test());  // "İlk return"
  

  // 8. Anonim Fonksiyonlar
  setTimeout(function () {
    console.log("Bu mesaj 2 saniye sonra gösterilecek.");
  }, 2000);
  
  // 9. Callback Fonksiyonlar
  function uzunSurenIslem(callback) {
    console.log("Uzun süren işlem başladı...");
    setTimeout(() => {
      console.log("Uzun süren işlem bitti.");
      callback();  // İşlem bittiğinde callback fonksiyonu çağrılır
    }, 3000);
  }
  

  
  // 10. Rest Parametreleri
  function toplaRest(...sayilar) {
    let toplam = 0;
    for (let sayi of sayilar) {
      toplam += sayi;
    }
    return toplam;
  }
  
  console.log(toplaRest(1, 2, 3, 4));  // 10
  console.log(toplaRest(5, 10));  // 15
  
  // 11. Immediately Invoked Function Expression (IIFE)
  (function () {
    console.log("Bu fonksiyon hemen çalışır!");
  })();
  
  // 12. Fonksiyonların Değeri (First-class Functions)
  let selamla = function () {
    return "Merhaba!";
  };
  
  function mesaj(fonksiyon) {
    console.log(fonksiyon());
  }
  
  mesaj(selamla);  // "Merhaba!" yazdırılır
  
  // 13. Arrow Fonksiyonlarda `this` Bağlamı
  let obje = {
    isim: "Eslem",
    yas: 25,
    selamVer: function () {
      setTimeout(() => {
        console.log(this.isim + " diyor ki: Merhaba!");  // this, obje'yi işaret eder
      }, 1000);
    },
  };
  
  obje.selamVer();  
  