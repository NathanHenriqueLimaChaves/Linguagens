/*
let js = 'incrivel';
console.log(40 + 8 + 23 - 10);


console.log("Jonas");
console.log(23);

let primeiroNome = "Jonas";
let pessoaUltimoNome = "Chaves";

console.log(primeiroNome);
console.log(pessoaUltimoNome);

let jonas_matilda = "JM";
let $function = 27;
let PI = 3.1415;
*/


// Seção 2 - Parte 12 - Tipos de Dados ***********************
/*
true;
console.log(true);
let javaScriptIsFun = true;
console.log(javaScriptIsFun);

console.log(typeof true);
console.log(typeof javaScriptIsFun);
console.log(typeof 28);
console.log(typeof "Nathan");

javaScriptIsFun = "Yes!";
console.log(javaScriptIsFun);

let myPetName;
console.log(typeof myPetName);

myPetName = "Luna";
console.log(myPetName);
*/


//Seção 2 - Parte 13 - let, const ans var **********************
/*
let age = 30;
age = 31;

const birthYear = 1998;
// birthYear = 1991;  -> irá dar erro
//const job; -> também dará erro

var job = "Programmer";
job = "Teacher"
*/


//Seção 2 - Parte 14 - Basic Operators *************************
/*
const ageJonas = 2037 - 1991;
const ageSarah = 2037 - 2018;
console.log(ageJonas, ageSarah);
*/
// melhorando esse código acima:
const now = 2037;
const ageJonas = now - 1991;
const ageSarah = now - 2018;
console.log(ageJonas, ageSarah);

// usando o console para mostrar vários valores
console.log(ageJonas * 2, ageJonas / 10, 2 ** 3);

// concatenando strings
const firstName = "Nathan";
const lastName = "Henrique";
console.log(firstName + ' ' + lastName);

// mais operadores 
let x = 10 + 5;
console.log(x); // 15
x += 10; // x = x + 10
console.log(x);  // 25
x *= 4; // x = x * 4
console.log(x);
x++;
console.log(x);
x--;
console.log(x);

// operadores de comparação
console.log(ageJonas > ageSarah); // deve retornar um valor booleano(true ou false)
console.log(ageJonas <= ageSarah); // false
console.log(ageSarah >= 18); // true

