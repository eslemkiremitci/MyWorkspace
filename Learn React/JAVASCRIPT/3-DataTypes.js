console.log( "------------------------------ DATA TYPES ------------------------------");
/*
DATA TYPES
-Bir değerin türünü tanımlar
-JavaScript'te iki ana kategoriye ayrılan veri tipleri vardır: Primitif (ilkel) veri tipleri ve Referans (nesne) veri tipleri.
-primitif (string, number, boolean, null, undefined, symbol, bigint)
-referans (object, array, function)
Primitif tipler doğrudan hafızada saklanır, referans tipler ise bellekteki adreslere işaret eder.
*/


//Primitif (İlkel) Veri Tipleri
//Primitif veri tipleri, JavaScript'te değişkenlerin tek bir değer tutmasını sağlar. Bu veri tipleri doğrudan hafızada saklanır.
console.log( "------------------------------ Primitif ------------------------------");
//String (Metin)
//Çift tırnak ("..."), tek tırnak ('...') veya template literal (şablon dizesi) ile tanımlanabilir: `...`.
let name = "Ahmet"; // Çift tırnak
let city = 'İstanbul'; // Tek tırnak
let greeting = `Merhaba ${name}`; // Template literal


//Number (Sayı)
let age = 25; // Tamsayı
let price = 99.99; // Ondalıklı sayı


//Boolean (Mantıksal)
let isOnline = true;
let isAdmin = false;


//Null
let emptyValue = null;


//Undefined: Bir değişken tanımlanmış ama değer atanmamışsa, varsayılan olarak undefined değerine sahip olur.
let notDefined;
console.log(notDefined); // undefined

//Symbol (ES6 ile geldi): Benzersiz ve değiştirilemez bir değer oluşturur. Genellikle nesne özelliklerini benzersiz yapmak için kullanılır.
let sym = Symbol("benzersiz");

//BigInt (ES2020 ile geldi): Çok büyük tamsayıları temsil eder. Sayıların aritmetiksel sınırlarını aşmak gerektiğinde kullanılır. n ekleyerek BigInt tanımlanır.
let bigNumber = 123456789012345678901234567890n;


//Examples:
console.log( "------------------------------ Examples Primitif ------------------------------");

let number = 10;
console.log( "z'nin tipi sting oldu mu? " + typeof number.toString());

let testScore = 60
let  IsItSuccessful = (testScore >= 50);
console.log(testScore);
console.log(IsItSuccessful);
console.log( "IsItSuccessful'un tipi: " + typeof IsItSuccessful);

let unassignedValue;
console.log(unassignedValue);
console.log( "unassignedValue'nun tipi: " + typeof unassignedValue);


let year = 1999;
let currentYear = new Date().getFullYear();
let age2 = currentYear - year;
console.log(age2);
console.log("age'ın tipi: " + typeof age2);


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