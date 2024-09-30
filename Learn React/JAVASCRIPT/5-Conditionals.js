console.log( "------------------------------ if - else if - else ------------------------------");

let score = 75;

if (score >= 90) {
  console.log("Notunuz: A");
} else if (score >= 80) {
  console.log("Notunuz: B");
} else if (score >= 70) {
  console.log("Notunuz: C");
} else {
  console.log("Notunuz: D");
}


console.log( "------------------------------ switch (durum) İfadesi ------------------------------");

let day = 2;

switch (day) {
  case 1:
    console.log("Pazartesi");
    break;
  case 2:
    console.log("Salı");
    break;
  case 3:
    console.log("Çarşamba");
    break;
  default:
    console.log("Geçersiz gün");
}


console.log( "------------------------------ Ternary (Koşul) Operatörü ------------------------------");

let age = 18;
let canVote = (age >= 18) ? "Oy kullanabilirsiniz." : "Oy kullanamazsınız.";
console.log(canVote); // Oy kullanabilirsiniz.



console.log( "------------------------------ Logical (Mantıksal) Operatörler ile Koşullar ------------------------------");

//Mantıksal Operatörler:
let age2 = 20;
let hasID = true;

if (age2 >= 18 && hasID) {
  console.log("Geçebilirsiniz.");
} else {
  console.log("Geçemezsiniz.");
}


let isWeekend = true;
let isHoliday = false;

if (isWeekend || isHoliday) {
  console.log("Tatildesiniz.");
} else {
  console.log("İşe gitmelisiniz.");
}


let isRaining = true;

if (!isRaining) {
  console.log("Dışarı çıkabilirsiniz.");
} else {
  console.log("Şemsiyenizi alın.");
}


console.log( "------------------------------ Falsy ve Truthy Değerler ile Koşullar ------------------------------");


let value = 0;

if (value) {
  console.log("Bu truthy bir değer.");
} else {
  console.log("Bu falsy bir değer.");
}
