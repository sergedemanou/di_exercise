/*
//example 1
for(let i = 0; i<100; i++){
    console.log(i)};
   
//    example 2
for (let i = 1; i < 1; i++){
    alert('i')
}; 
//ici on aura un break car la condition n'est pas respectée

//example 3
for (let i=0; i<=100; i++){if (i%2==0) {console.log(i)}};
example4


for (let i=120; i<=181 ; i++) { if (i%2==0) {console.log(i + " even") }
else {console.log(i + " odd")}}

for (let i=0; i<=15; i++) { if (i%2==0){console.log(i + " is even")} else {console.log(i + " is odd")}}

*/

var names = ["john", "sarah", 23, "Rudolf", 34];
for (let i = 0; i < names.length; i++) 
{
    if (typeof(names[i])!= "string"){
        continue;}
        else if (typeof(names[i]) == "string"){
            if(names[i].charAt(0) == names[i].charAt(0).toUpperCase()){
                console.log(names[i]);
            }
            else{console.log(names[i].charAt(0).toUpperCase() + names[i].substring(1,names[1].length))}
        }
}
    
    

