
// funcion map, devuelve una lista de las mismas dimeciones, para cada elemento hace una operacion 

const square = x => x * x;
const squares = numbers => numbers.map(x => x * x);
// const squares = numbers => numbers.map(square);

const numbers = [1,2,3,4,5,6,7];
console.log(squares(numbers));

console.log(numbers)

// sqrt 

const root = numbers => numbers.map(x => x ** 0.5);

console.log(root(numbers))