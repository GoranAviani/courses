<?php
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

$userInput = "8";
$result = array();

for ($a = 1; $a < $userInput +1; $a++){
    echo $a."<br/>";
    echo $a * $a ."<br/>";
    array_push($result,$a, $a * $a);
}

foreach ($result as $res){
    echo $res;
}

?>
