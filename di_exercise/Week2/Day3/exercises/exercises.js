/*
 Exercise 1

 let colors = ["yellow","green","white","blue"];
 let suffix = ["st","nd","rd", "th"]
for (let i= 0; i<colors.length; i++){
    console.log("My#1 choice is " + colors[i])
}
for (let i= 0; i<colors.length; i++){
console.log(`My ${i+1}${suffix[i]} choice is ${colors[i]} `)
}
*/

/*
//Exercise 2
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
let x = [names[0].charAt(0)];
for (let i=1; i<names.length; i++){
    x.push(names[i].charAt(0));
    console.log(x.sort().join(""));
}
second option

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
let x = names.sort();
console.log(x)
let society_name = "";

for ( let i=0; i<names.length; i++){
    console.log(names[i].charAt(0))
    society_name =  society_name + names[i].charAt(0);

}

 console.log(society_name);
 */

/*
// Exercise 3

 let n = parseInt(prompt('enter a number')))
 while (n<10){
     n = prompt('Enter another number')
 }
*/
/*
//Exercise 4
let people = ["Greg", "Mary", "Devon", "James"];

for (let i= 0; i<people.lenhgt; i++){
    console.log(i)
}
let b = people.splice(0,1)
console.log(b)
console.log(people)
people.splice(2,1,"Jason")
console.log(people)
people.push("Serge")
console.log(people)
for (let i= 0; i<people.length;i++){
    console.log(i);
    
}

console.log(people)

*/


// Daily_Challenge

 const numbers = [5,0,9,1,7,4,2,6,3,8];
 let x = numbers.toString();
 console.log(x);