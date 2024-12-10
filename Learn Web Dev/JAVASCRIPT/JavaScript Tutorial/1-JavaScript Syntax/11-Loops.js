for (başlatma; koşul; artırma / azaltma) {
  // Tekrarlanacak kod
}


for (let i = 0; i < 5; i++) {
  console.log("i'nin değeri: " + i);
}





while (koşul) {
  // Tekrarlanacak kod
}


let ii = 0;
while (ii < 5) {
  console.log("ii'nin değeri: " + ii);
  i++;
}





do {
  // Tekrarlanacak kod
} while (koşul);


let iii = 0;
do {
  console.log("i'nin değeri: " + iii);
  i++;
} while (iii < 5);





for (değişken in nesne) {
  // Tekrarlanacak kod
}


let araba = { marka: "Toyota", model: "Corolla", yil: 2020 };
for (let ozellik in araba) {
  console.log(ozellik + ": " + araba[ozellik]);
}



for (değişken of dizi) {
  // Tekrarlanacak kod
}


let meyveler = ["Elma", "Muz", "Çilek"];
for (let meyve of meyveler) {
  console.log(meyve);
}


//Döngüden Çıkmak (break)

for (let i = 0; i < 10; i++) {
    if (i === 5) {
      break;  // i 5'e ulaştığında döngüden çıkar
    }
    console.log(i);
  }

  
//Döngünün Bir Adımını Atlamak (continue)

for (let i = 0; i < 10; i++) {
    if (i === 5) {
      continue;  // i 5 olduğunda o adım atlanır
    }
    console.log(i);
  }
  

//Nesneleri ve Dizileri Döngü ile Gezme

let ogrenci = { ad: "Ali", yas: 20, ders: "Matematik" };
for (let ozellik in ogrenci) {
  console.log(ozellik + ": " + ogrenci[ozellik]);
}

let sayilar = [1, 2, 3, 4, 5];
for (let sayi of sayilar) {
  console.log(sayi);
}


while (true) {
    console.log("Bu bir sonsuz döngüdür");
    // Bu döngü asla durmaz!
  }
  
