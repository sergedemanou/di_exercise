//programme pour déterminer si l'utilisateur est majeur


let age = parseInt(prompt("how old are you?"));
if (age ==18 ){
    alert("Congratulations on your first year of driving. Enjoy the ride!");
}
else if (age < 18){
    alert("Sorry, you are too young to drive this car. Powering off");
}
else{
    alert("Powering On. Enjoy the ride");
}

