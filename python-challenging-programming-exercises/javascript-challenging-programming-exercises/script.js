//01_find_all_numbers
    /*
    var list = [];
    var i;
    for (i = 2000; i < 3001; i++) {
        list.push(i);
    }
    console.log(list)
    */

    /*
    function findAllNumbers(a,b){
        var i;
        var list = [];
        for (i = a; i < b; i++) {
         list.push(i);
        }
        return list
        }
    console.log(findAllNumbers(2000,3001))
    */

    /*
    first = 2000
    second = 3000
    var findAllNumbersVar = (function(a,b) {
        var result = [];
        var i;
        for (i=a; i<b ; i++){
            result.push(i);
        }
        return result;
    })(first, second)


    console.log(findAllNumbersVar)
    */
/*# Question 3
# Level 1
# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
*/
/*
function findAllNumbers(a,b){
        var i;
        var result = 1;
        for (i = a; i < b + 1; i++) {
            result = (result * i);
        }
        return result
        }
console.log(findAllNumbers(1,8))
*/
/*
# Question 3
# Level 1
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number
#  between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
*/
/*
function integralNUmbers(number){
    var i;
    var resultDict = {};
    for (i = 1; i < number +1; i++){
        resultDict[i] = (i*i);

    }
    return resultDict
}

console.log(integralNUmbers(8))
*/
/*
# Question 4
# Level 1
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains
# every number. #Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple
*/
/*
function tupple(sequence) {
    var sequencelist = [];
    sequenceList = sequence.split(",");
    var i;

    console.log(sequenceList.length)
    for (i = 0; i < 3; i++) {

    }
    return sequenceList
}

console.log(tupple("34,67,55,33,12,98"))
*/

/*# Question 5
# Level 1
# Question:
# Define a class which has at least two methods: getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


*/

/*
# Question 6
# Level 1
#  Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0,
# it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console input.
*/

/*
function formula(numberList){
    var C = 50;
    var H = 30;
    var formulaList = [];
    var i = 0;
    var resultList = [];
    formulaList = numberList.split(",")

    for (i = 0; i<formulaList.length; i++){
        resultList.push(Math.round(Math.sqrt([(2 * C * formulaList[i])/H])))
    }

    return resultList;
}

console.log(formula("100,150,180"))
*/

/*
# Question 7
# Level 2
# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1,2 , 3, 4], [0, 2, 4, 6, 8]]
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
*/
/*
function array2D(numbers){
    var i;
    var y;
    var numbersList = [];
    numbersList = numbers.split(",");
    console.log(numbersList[0])
    console.log(numbersList[1])
    var resultList = [];
    var resultOfRound = [];
    for ( i = 0; i < numbersList[0]; i++){
        resultOfRound = []

        for (y=0; y < numbersList[1]; y++){
           resultOfRound.push(i*y);
        }
        resultList.push(resultOfRound)

    }
    return resultList
}

console.log(array2D("3,5"))
*/
/*
# Question 8
# Level 2
# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
# sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
*/

/*
function inputConsole(event) {
    //prevent Default to prevent quick refresh of the page
  event.preventDefault();
  var data = document.getElementById("userInfoData");
  console.log(data.value);
  console.log(sorting(data.value))
}


function sorting(text){
    text = text.split(",");
    return text.sort()
}
*/

/*
# Question 9
# Level 2
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
*/
/*
function inputConsole(event){
    event.preventDefault();
    let inputUser = document.getElementById("userInfoData");
    inputUser = inputUser.value;

    result = inputUser.split(',');
    console.log(result.length)

    let i;
    for (i = 0; i < result.length; i++){
        console.log(result[i].toUpperCase())

    }
}
*/

/*
# Question 10
# Level 2
# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing
# all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data
*/

/*
function uniq(a) {
   return Array.from(new Set(a));
}

function inputConsole(event){
    event.preventDefault();
    let inputUser = document.getElementById("userInfoData");
    inputUser = inputUser.value
    console.log(inputUser)
    inputUser = inputUser.split(" ");
    console.log(inputUser)
    inputUser.sort();
    console.log(uniq(inputUser))

}

*/

/*
# Question 11
# Level 2
# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are
# divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
*/

/*
function checkIfDivisable(number){
   if (parseInt(number,2) % 5 === 0){
        return(number)
    }
}


function inputConsole(event){
    event.preventDefault();
    let inputUser = document.getElementById("userInfoData");

    console.log(inputUser.value)
    inputUser = inputUser.value
    inputUser = inputUser.split(",");

    let i;
    for (i = 0; i<inputUser.length; i++){
        console.log(checkIfDivisable(inputUser[i]));
    }

}
*/

/*
# Question 12
# Level 2
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an
# even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
*/


let i;
let x;
let result = [];
let isEven = false;
for (i=1; i<3001;i++){
    isEven = true;

    for (x = 0; x < i.toString().length; x++){
        console.log(i)
        if (i[x] % 2 == 0){
            console.log("ok")
        }else{
            console.log("neok")
            isEven = false;
        }
    }

    if (isEven = true) {
        result.push(i);
    }
}

//console.log(result)