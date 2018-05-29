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

function integralNUmbers(number){
    var i;
    var resultList = []
    for (i = 1; i < number +1; i++){
        resultList.push(i);
        resultList.push(i*i);
    }
    return resultList
}

console.log(integralNUmbers(8))