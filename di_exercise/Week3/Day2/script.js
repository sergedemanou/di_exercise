 
/*       Exercise 1
 Write a JavaScript function to add rows to a table. Use the code below as a base
 
 
 
 
 let table = document.getElementById('sampleTable');
let i = 3;
function insert_Row () {
    let tr = document.createElement('tr');
    let td1 = document.createElement('td');
    let td2 = document.createElement('td');
    let x=i++;
    td1.innerText = `Row ${x} Cell1`;
    td2.innerText = `Row ${x} Cell2`;
    tr.appendChild(td1);
    tr.appendChild(td2);
    table.appendChild(tr);

}


*/



 /*      Exercise 2
Add a few event listener to the button. The event listeners should change the style of the button

<button id="jsstyle">Style</button> */
/*
  let butt = document.getElementById('jsstyle');
  butt.addEventListener('click', ChangeStyle);
  butt.addEventListener('mouseover', ChangeBackground);
  butt.addEventListener('mouseout', ChangeBorder);
  function ChangeStyle() {
       butt.style.color = 'pink';
  }
function ChangeBackground(){
    butt.style.backgroundColor = 'orange';
}
function ChangeBorder(){
    butt.style.border = '3px purple solid';
}
document.getElementById('button').onclick = function() {
    alert('Click!');
};
*/


//Exercice 1: Modifier L'article


//1.Donnez à tous les paragraphes à l'intérieur de la <article>balise la classe de para_article.//
 let p = document.querySelectorAll('p');

 for (let i = 0; i<p.length; i++){
     p[i].setAttribute('class', 'para_article');
 }

 //2.Supprimez le dernier paragraphe de l'article.
 p[p.length-1].remove();

 //3.Ajoutez un écouteur d'événements pour que lorsque vous cliquez sur h2, il soit supprimé du DOM.

 /*function rem(x){
     x.remove();
 }*/

        //2emethode

 let h2 = document.querySelector('h2');
 function rem(){
    h2.remove();
 }

 //4.Set the font size of the h1 to be a random pixel size from 0 to 100.
  let h1 = document.querySelector('h1');
  let be = Math.floor(Math.random()*100);

h1.style.fontSize = be + 'px';
//5.Hide the 1st paragraph, when it’s clicked. (use the display property )
function del(){
    p[0].style.display = 'none';
}
p[0].addEventListener('click', del);


//6.Get the values from the inputs and append them to the end of the html, inside a table.
let inputs = document.querySelector('input');
let bro = [];
for (let i = 0;i<inputs.length; i++){
    bro.push(inputs[i].value);
}
function blabla(w){

}

//7.Bonus: Fade out the 2nd paragraph over 2000 milliseconds, when it’s clicked.

p[1].addEventListener('click',fadeOut);
function