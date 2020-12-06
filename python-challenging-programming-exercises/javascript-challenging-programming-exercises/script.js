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


function Faktorijel(b){
        var i;
        var result = 1;
        for (i = 1; i < b + 1; i++) {
            result = (result * i);
        }
        return result
        }
console.log(Faktorijel(9))



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
 Question 12
 Level 2
 Question:
 Write a program, which will find all such numbers between 1000 and 3000
(both included) such that each digit of the number is an even number.
 The numbers obtained should be printed in a comma-separated sequence on a single line.
 Hints:
 In case of input data being supplied to the question, it should be assumed to be a console input.
*/
/*
function inputConsole(event) {
    let number;
    let x;
    let result = [];
    let isEven = false;

    event.preventDefault();
    let inputUser = document.getElementById("userInfoData");

    for (number = 1; number < inputUser.value; number++) {
        isEven = true;
        numberString = number.toString()


        for (x = 0; x < numberString.length; x++) {
            //console.log(numberString[x])

            if (numberString[x] % 2 == 0) {
                //do nothing here
            } else {
                isEven = false;
            }
        }

        if (isEven === true) {
            result.push(numberString);
        }

    }
    console.log(result.toString())
}
*/

/*
# Question 13
# Level 2
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
*/

/*
function inputConsole(event){
    event.preventDefault();
    let numbers = 0;
    let letters = 0;

    let x;
    let userInput = document.getElementById("userInfoData")


    for (x = 0; x < userInput.value.length; x++) {
       // console.log(userInput.value[x])

            if (/^[a-zA-Z]/.test(userInput.value[x])){
            letters += 1;
            }else if (/^[1-9]/.test(userInput.value[x])){
            numbers +=1;
            }
    }


    console.log("LETTERS "+letters)
    console.log("NUMBERS "+numbers)

}

*/

/*
# Question 14
# Level 2
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
*/
/*
function inputConsole(event){
    event.preventDefault()
    let userInput = document.getElementById("userInfoData");

    let x;
    let upperLetters = 0;
    let lowerLetters = 0;


    for (x = 0; x < userInput.value.length; x++){

        if (/^[a-z]/.test(userInput.value[x])){
            lowerLetters += 1;
        }else if (/^[A-Z]/.test(userInput.value[x])){
            upperLetters += 1;
        }


    }

    console.log("UPPER CASE " + upperLetters)
    console.log("LOWER CASE " + lowerLetters)
}

*/

/*
# Question 15
# Level 2
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
*/

/*
function inputConsole(event) {
    event.preventDefault();
    let userInput = document.getElementById("userInfoData");
    userInput = userInput.value;

    result = parseInt(userInput) + parseInt(userInput + userInput)
        + parseInt(userInput+userInput+userInput) + parseInt(userInput+userInput+userInput+userInput);

    console.log("resultat " + result)
}
*/

/*
# Question 16
# Level 2
# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9 and 1,9,25,49,81
*/
/*
function inputConsole(event){
    event.preventDefault();
    let userInput = document.getElementById("userInfoData");
    userInput = userInput.value;
    userInput = userInput.split(",");

    let x;
    let resultNumber = [];
    let resultNUmberSquare = [];
    console.log(userInput);

    for (x = 0; x < userInput.length; x++){
        if (userInput[x] % 2 != 0){
            resultNumber.push(userInput[x])
            resultNUmberSquare.push(parseInt(userInput[x]) **2)
        }
    }
    console.log(resultNumber.toString() + " and " +resultNUmberSquare.toString())

}
*/
/*
# Question 18
# Level 3
# Question:
# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
*/

/*
function inputConsole(event) {
    event.preventDefault();
    let userInput = document.getElementById("userInfoData");
    userInput = userInput.value;

    userInput = userInput.split(",");

    let x;
    let hasLowecase = false;
    let hasUppersase = false;
    let hasNumber = false;
    let hasSpecialCharacter = false;
    let result = []
    const specialChar = /^[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]*$/;

    for (i = 0; i < userInput.length; i++) {
        hasLowecase = false;
        hasUppersase = false;
        hasNumber = false;
        hasSpecialCharacter = false;
        //console.log(userInput[i])

        if (userInput[i].length < 6 || userInput[i].length > 12) {
            console.log("Password must have from 6 to 12 characters")
        } else {

            for (x = 0; x < userInput[i].length; x++) {

                if (/^[a-z]/.test(userInput[i][x])) {
                    hasLowecase = true;
                }

                if (/^[A-Z]/.test(userInput[i][x])) {
                    hasUppersase = true;
                }

                if (/^[1-9]/.test(userInput[i][x])) {
                    hasNumber = true;
                }

                if (userInput[i][x].match(specialChar)) {
                    hasSpecialCharacter = true;
                }
            }
        }


        if (hasLowecase == true && hasUppersase == true && hasNumber == true && hasSpecialCharacter == true) {
            result.push(userInput[i])
        }
    }
    console.log(result)

}
*/


