console.log( "------------------------------ OPERATORS ------------------------------");
/*
1. Atama Operatörleri
2. Aritmetik Operatörler
3. Karşılaştırma Operatörleri
4. Mantıksal Operatörler
5. Bit Düzeyi (Bitwise) Operatörler
6. Koşul (Ternary) Operatörü
7. Tür Operatörü (typeof)
8. Virgül Operatörü
*/
// 1. Atama Operatörleri
let x = 10;       // Basit atama
x += 5;           // x = x + 5, yani x şimdi 15
x -= 3;           // x = x - 3, yani x şimdi 12
x *= 2;           // x = x * 2, yani x şimdi 24
x /= 4;           // x = x / 4, yani x şimdi 6
x %= 5;           // x = x % 5, yani x şimdi 1

console.log("Atama Operatörleri:", x);

// 2. Aritmetik Operatörler
let a = 10 + 5;   // Toplama, a = 15
let b = 10 - 5;   // Çıkarma, b = 5
let c = 10 * 2;   // Çarpma, c = 20
let d = 10 / 2;   // Bölme, d = 5
let e = 10 % 3;   // Modül, e = 1

console.log("Aritmetik Operatörler:", a, b, c, d, e);

// Arttırma ve Azaltma Operatörleri
let f = 5;
f++;              // Arttırma, f = 6
f--;              // Azaltma, f = 5
console.log("Arttırma ve Azaltma:", f);

// 3. Karşılaştırma Operatörleri
let isEqual = (5 == "5");    // Eşittir, true (tip dönüştürülür)
let isStrictEqual = (5 === 5); // Sıkı eşittir, true (tip ve değer aynı)
let isNotEqual = (5 != "6"); // Eşit değildir, true
let isStrictNotEqual = (5 !== "5"); // Sıkı eşit değildir, true (tip farklı)
let isGreater = (10 > 5);    // Büyüktür, true
let isLess = (10 < 15);      // Küçüktür, true
let isGreaterOrEqual = (10 >= 10); // Büyük veya eşittir, true
let isLessOrEqual = (5 <= 10);     // Küçük veya eşittir, true

console.log("Karşılaştırma Operatörleri:", isEqual, isStrictEqual, isNotEqual, isStrictNotEqual, isGreater, isLess, isGreaterOrEqual, isLessOrEqual);

// 4. Mantıksal Operatörler
let logicalAnd = (true && false); // Mantıksal ve, false
let logicalOr = (true || false);  // Mantıksal veya, true
let logicalNot = (!true);         // Mantıksal değil, false

console.log("Mantıksal Operatörler:", logicalAnd, logicalOr, logicalNot);

// 5. Bit Düzeyi Operatörler
let bitwiseAnd = (5 & 1);     // Bit düzeyinde ve, 1
let bitwiseOr = (5 | 1);      // Bit düzeyinde veya, 5
let bitwiseXor = (5 ^ 1);     // Bit düzeyinde XOR, 4
let bitwiseNot = (~5);        // Bit düzeyinde değil, -6
let leftShift = (5 << 1);     // Bit kaydırma (sola), 10
let rightShift = (5 >> 1);    // Bit kaydırma (sağa), 2

console.log("Bit Düzeyi Operatörler:", bitwiseAnd, bitwiseOr, bitwiseXor, bitwiseNot, leftShift, rightShift);

// 6. Koşul (Ternary) Operatörü
let age = 18;
let canVote = (age >= 18) ? "Evet, oy kullanabilir" : "Hayır, oy kullanamaz";
console.log("Koşul Operatörü:", canVote);

// 7. Tür Operatörü (typeof)
let typeOfVariable = typeof 5;      // number
let typeOfString = typeof "hello";  // string
let typeOfBoolean = typeof true;    // boolean

console.log("Tür Operatörü:", typeOfVariable, typeOfString, typeOfBoolean);

// 8. Virgül Operatörü
let h = (1, 2, 3, 4); // Son değer olan 4 döner
console.log("Virgül Operatörü:", h);
