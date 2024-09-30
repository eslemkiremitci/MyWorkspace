//Object (Nesne) Tanımlama

//Nesne Literalleri ile Tanımlama
let araba = {
  marka: "Toyota",
  model: "Corolla",
  yil: 2021,
  calistir: function () {
    console.log("Araba çalışıyor...");
  },
};

console.log(araba.marka);
araba.calistir();
console.log(araba["model"]); 
araba.renk = "Kırmızı";  // Yeni özellik ekledik
araba.marka = "Honda";   // Var olan özelliği güncelledik
console.log(araba);  // { marka: "Honda", model: "Corolla", yil: 2021, renk: "Kırmızı" }
delete araba.model;  // "model" özelliği silinir
console.log(araba);  // { marka: "Honda", yil: 2021, renk: "Kırmızı" }

console.log(Object.keys(araba));  // ["marka", "yil", "renk"]
console.log(Object.values(araba));  // ["Honda", 2021, "Kırmızı"]
console.log(Object.entries(araba)); // [["marka", "Honda"], ["yil", 2021], ["renk", "Kırmızı"]]


let yeniAraba = Object.assign({}, araba);
console.log(yeniAraba);  // Kopyalanmış nesne


let yeniOgrenci = { ...ogrenci };
console.log(yeniOgrenci);  // Kopyalanmış nesne


//new Object() ile Tanımlama
let kisi = new Object();
kisi.ad = "Eslem";
kisi.yas = 30;
console.log(kisi.ad);


console.log("----------------------------------------------------------------------------------------------------------------");


// Kullanici nesnesi tanımlandı
let kullaniciA = {
  ad: "Eslem",
  soyad: "Kiremitci",
  yas: 38,
  adres: {
    sehir: "kocaeli",
    ilce: "gebze",
  },
  hobiler: ["sinema", "spor"],
};

let kullaniciB = {
  ad: "İlknur",
  soyad: "Kiremitci",
  yas: 38,
  adres: {
    sehir: "kayseri",
    ilce: "develi",
  },
  hobiler: ["sinema", "doğa yürüyüşü"],
};

let sonuc;

// Kullanıcı A'dan bilgileri alma
sonuc = kullaniciA.ad;
console.log("Ad:", sonuc);

sonuc = kullaniciA.soyad;
console.log("Soyad:", sonuc);

sonuc = kullaniciA["yas"];
console.log("Yaş:", sonuc);

sonuc = kullaniciA.adres.sehir;
console.log("Şehir:", sonuc);

sonuc = kullaniciA.adres.ilce;
console.log("İlçe:", sonuc);

sonuc = kullaniciA.hobiler[0];
console.log("Hobi 1:", sonuc);

sonuc = kullaniciA.hobiler[1];
console.log("Hobi 2:", sonuc);

// Birden fazla kullanıcıyı bir dizi içinde topluyoruz
let kullanicilar = [kullaniciA, kullaniciB];

// Kullanıcılar dizisindeki 1. kullanıcının adı
sonuc = kullanicilar[1].ad;
console.log("Kullanıcı B Adı:", sonuc);

// Ürünler dizisi ve içinde nesneler
let urunler = [
  {
    urun_adi: "samsung s22",
    urun_fiyat: 13000,
  },
  {
    urun_adi: "samsung s23",
    urun_fiyat: 15000,
  },
];

// Ürünlerin 0. indeksindeki ürünün adını almak
sonuc = urunler[0].urun_adi;
console.log("Ürün Adı:", sonuc); // "samsung s22"


let ogrenci = {
    ad: "Ali",
    soyad: "Yılmaz",
    yas: 20,
    tamAd: function() {
      return this.ad + " " + this.soyad;
    }
  };
  
  console.log(ogrenci.tamAd());  // "Ali Yılmaz"


  console.log("------------------------- Nesneleri Dolaşma (Object Iteration) ----------------------------------")
  
  for (let ozellik in ogrenci) {
    console.log(ozellik + ": " + ogrenci[ozellik]);
  }
  
  
  
