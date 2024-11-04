//Referans (Nesne) Veri Tipleri
//Referans veri tipleri, hafızada saklanan adresleri referans alır. Değerlerin kendisi yerine referansları saklanır.
//Yani değişken adres tutar. verinin bulunduğu adresi
console.log( "------------------------------ Referans  ------------------------------");
//Object (Nesne)
let person = {
    name: "Mehmet",
    age: 30,
    isMarried: false
};

//Array (Dizi)
let numbers = [1, 2, 3, 4];
let colors = ["kırmızı", "yeşil", "mavi"];

//Function (Fonksiyon)
function greet() {
    console.log("Merhaba!");
}


console.log( "------------------------------ DATA TYPES EXAMPLES ------------------------------");
console.log(typeof "Merhaba"); // string
console.log(typeof 42); // number
console.log(typeof true); // boolean
console.log(typeof null); // object (bu JavaScript'in tarihi bir hatasıdır)
console.log(typeof undefined); // undefined

console.log( "------------------------------ parseFloat() - parseInt() ------------------------------");
//parseFloat(), bir metin (string) ifadesini ondalıklı bir sayıya (float) dönüştürmek için kullanılır.
let sayi1 = "3.14";
let sayi2 = "10.99abc";

console.log(parseFloat(sayi1)); // 3.14
console.log(parseFloat(sayi2)); // 10.99 ('abc' kısmını görmezden gelir)
console.log(parseFloat("abc123")); // NaN

//parseInt(), bir metin ifadesini tamsayıya (integer) dönüştürmek için kullanılır.
let sayi3 = "42";
let sayi4 = "10abc";
let sayi5 = "10.99";

console.log(parseInt(sayi3)); // 42
console.log(parseInt(sayi4)); // 10 ('abc' kısmını görmezden gelir)
console.log(parseInt(sayi5)); // 10 (ondalık kısmı görmezden gelir)


let binary = "1010"; // Binary sayı (2 tabanında)
let hex = "1F"; // Hexadecimal sayı (16 tabanında)

console.log(parseInt(binary, 2)); // 10 (binary'den 10'luk tabana çevirir)
console.log(parseInt(hex, 16)); // 31 (hexadecimal'den 10'luk tabana çevirir)

console.log(parseInt("abc42")); // NaN

console.log(parseInt("9.99")); // 9