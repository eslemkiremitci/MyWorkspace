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
let name = "Eslem"; // Çift tırnak
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
