/*Difference between var & let
var y = 4;
console.log(y)

var y ;
console.log(y)

for (var i = 1; i<=4; i++){
    console.log(i)
}
console.log(i)

for (let j = 1; j<=4; j++){
    console.log(j)
}
console.log(j)
*/

//exercise 1
//myage = x;
//agemom = x*2;
//agedad = 1.2(x*2);
/*
function display_age (myage){
    console.log(`The age of my mum is ${myage*2} and the age of my dad is ${(myage*2*1.2)}`)
    return;
}

display_age(10);
*/
/*
function display_age (myage){
    let result = `The age of my mum is ${myage*2} and the age of my dad is ${(myage*2*1.2)}`
    return result;
}

let x = display_age(5)
console.log(x)

//Exercise 2
 function display_mom_age(myage){
     return myage*2;
 }
 display_mom_age(30)//30*2
 console.log( display_mom_age(20));
*/




//Exercises XP

 //Exercise 1
/*
 function cheeckDriverAge(age) {
    
    age = prompt("What is your age?");

    if (Number(age) < 18) {
        alert("Sorry, you are too yound to drive this car. Powering off");
    } else if (Number(age) > 18) {
        alert("Powering On. Enjoy the ride!");
    } else if (Number(age) === 18) {
        alert("Congratulations on your first year of driving. Enjoy the ride!");
    }
    
    
  }
cheeckDriverAge(18)
*/
/*
 // Exercise 2
 function Is_Blank(str)
 {
     if(str.length==0){
     return true;
     }
     else{return false;} 
     
    
 }
console.log(Is_Blank('ok'));
*/

/*
//Exercise 3
function abbrev_name(str){
    let str1 = str.trim().split(" ");
    let str2 = str1[0] + " " + str1[1].charAt(0);
    return str2;

}
console.log(abbrev_name('demanou serge'))

*/

//Exercise 4
function SwapCase(letters){
    for (let i=o; i<letters.length; i++)
    let str = letters.toLowerCase();
    let str1 = letters.toUpperCase();
    let word = str1 + str
     if{
         st
     }
    }