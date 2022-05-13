const isEven = x => x % 2 === 0; 

const isOdd = x => x % 2 !== 0;

// las comparaciones son con === (== tambien sirve pero es menos confiable, no usar) 

const evenNumbers = numbers => {

   // return numbers.filter(x => isEven(x));

   return numbers.filter(isEven);
}

// .filter() es funcion de js, sirve para revisar que los datos cumplan un criterio

const OddNumbers = numbers => numbers.filter(x=> !isEven(x));

const numbers = [1,2,3,4,5,6,7];

console.log(evenNumbers(numbers));
console.log(OddNumbers(numbers));