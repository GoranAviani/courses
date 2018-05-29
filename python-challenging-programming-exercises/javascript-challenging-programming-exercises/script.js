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

