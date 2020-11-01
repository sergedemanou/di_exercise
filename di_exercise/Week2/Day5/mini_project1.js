let display = document.getElementById('display');
console.log(display);
let display_value = display.innerHTML;
console.log(display_value);
//display.innerHTML = 'hello';

let current = [];
function my_f(num){
	let display = document.getElementById('display');
	if (num === '=') {
		let operator_position;
		let numb = '';
		
		for(let i of current){
			/*
			if(typeof(i) === 'number'){
				numb+=i;
			}
			else if (typeof(i) === 'string') {
				operator_position=current.indexOf(i);
				console.log(i + ' '+ operator_position);
				var operator = i;

			}
			else break;6
		*/
			numb+=i;
		}
		let total = eval(numb);
		console.log('TOTAL '+total);
		display.innerHTML = total;
		/*
		console.log(numb);
		let numb1 = numb.substring(0, operator_position);
		let numb2 = numb.substring(operator_position, numb.length);
		console.log(numb1 + ' '+numb2);
		if (operator == '+') { console.log(Number(numb1)+Number(numb2));}
		if (operator == '-') { console.log(Number(numb1)-Number(numb2));}
		if (operator == '*') { console.log(Number(numb1)*Number(numb2));}
		if (operator == '/') { console.log(Number(numb1)/Number(numb2));}*/

	}
	else{
		
		current.push(num);
		display.innerHTML = current.join('');	
	}
	

	//console.log(two);
	//two.innerHTML =200;
	console.log(current);
}
