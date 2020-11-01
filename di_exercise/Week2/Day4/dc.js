/*Daily Challenge : Bubble Sort
const numbers = [5,0,9,1,7,4,2,6,3,8];

Using the .toString() method, convert the array to a string.
Using the .join(), convert the array to a string. Try passing different values into the join.
Eg .join(“+”), .join(” “), .join(“”)
Bonus : Sort the array numbers in descending order using for loops (Not using built-in sort methods).
The output should be: [9,8,7,6,5,4,3,2,1,0]
Hint: The algorithm is called “Bubble Sort”
Use a temporary variable to swap values in the array.
Use 2 “nested” for loops (Nested means one inside the other).
Add comments and console.log the result for each step, it will help you understand.
Requirement: Don’t copy paste solutions from Google
*/
const numbers = [5,0,9,1,7,4,2,6,3,8];

let str = numbers.toString();
let str1 = numbers.join();





function sort(x)
{
    var numb;
    var n = x.length-1;
    do {
        numb = false;
        for (var i=0; i < n; i++)
        {
            if (x[i] < x[i+1])
            {
               var okay = x[i];
               x[i] = x[i+1];
               x[i+1] = okay;
               numb = true;
            }
        }
        n--;
    } while (numb);
 return x; 
}
console.log(sort);

