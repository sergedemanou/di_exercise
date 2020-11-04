//1.Create an array of planets of the solar system//

let solarSystem = ['mercure', 'venus','terre', 'mars', 'jupiter','saturne', 'uranus','neptune'];
//2.For each planet, in the array, create a div using createElement. This div should have a class named ‘planet’.//

for  (let planet in solarSystem) {
    let div = document.createElement('div');
    console.log('planet');
    div.setAttribute('class','planet');
    console.log(div);
}
//3.Each planet should have a different background color. (Hint: add a new class to each planet)//

let solarSystem = {
    mercure:{'color': 'orange'};
    venus:{'color': 'orange'};
    terre:{'color': 'orange'}
    mars:{'color': 'orange'}
    jupiter:{'color': 'orange'}
    saturne:{'color': 'orange'}
    uranus:{'color': 'orange'}
    neptune:{'color': 'orange'}


}