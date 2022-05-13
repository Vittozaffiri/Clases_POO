

const sumOf = numbers => {

    return numbers.reduce((acc,x)=> acc + x)//x,0 aca se pone el valor inicial si necesito;
}

const numbers = [1,2,3,4,5,6,7];

console.log(sumOf(numbers));


const multOf = numbers => {

    return numbers.reduce((acc,x)=>acc*x);
}

console.log(multOf(numbers));