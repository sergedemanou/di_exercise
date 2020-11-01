// Using the .toString() method, convert the array to a string.

const numbers = [5,0,9,1,7,4,2,6,3,8];
let val  = numbers[0];
for(let i = 1; i< numbers.length; i++){
    val = val.toString() + numbers[i].toString();
}
console.log(val);

/* Using the .join(), convert the array to a string. Try passing different values into the join.
Eg .join(“+”), .join(” “), .join(“” ) */

console.log(numbers.join('').toString());

console.log(numbers.join(' + ').toString());

console.log(numbers.join(' ').toString());

// bonus 

/*   
 Sort the array numbers in descending order using for loops (Not using built-in sort methods).
The output should be: [9,8,7,6,5,4,3,2,1,0]
*/
let temp = numbers[0];
let tab = [];
for(let i = 1; i<numbers.length; i++){
   for() 
}