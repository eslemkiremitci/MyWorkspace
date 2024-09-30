console.log( "------------------------------ VARIABLES ------------------------------");
/*
VARIABLES

Değişkenler (variables) bir veri saklama yapısıdır. RAM'de saklanır. Geçici. 
JavaScript'te değişken tanımlamak için üç temel anahtar kelime kullanılır.(var, let, const)
Türkçe karakter kullanılmaz. Arada boşluk olmaz. Sayı ile başlayamaz.
String için "" ya da '' kullanılabilir.
*/


var x = "Var değişkeni sadece o fonksiyon içinde geçerli olur. (function scope)";
console.log(x); // eski yöntem, hataya açık.

//2015 yılında ECMAScript 6 (ES6) ile gelen yeni bir değişken tanımlama yöntemidir.
//Blok kapsamına (block scope) sahiptir. Aynı ismi birden fazla kez kullanmanıza izin vermez. Bu, kodun daha temiz ve güvenli olmasını sağlar.
let y = 10;
if (true) {
    let y = 20;
    console.log("Blok içi y: " + y);
}
console.log("Blok dışı y: " + y);

//Yine ES6 ile gelen bir tanımlama yöntemidir.
//Blok kapsamına sahiptir.
//Değer atandıktan sonra değiştirilemez. Yani, sabit bir değer (constant) tanımlamak için kullanılır.
//Ancak, const ile tanımlanan nesnelerin (object) veya dizilerin (array) içeriği değiştirilebilir.
const z = 15; // z = 20; // Hata verir çünkü `const` ile tanımlanan bir değeri değiştiremezsiniz.

const arr = [1, 2, 3];
arr.push(4); // Bu geçerli, çünkü dizinin içeriğini değiştirdik.
console.log(arr); // [1, 2, 3, 4]


