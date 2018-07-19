<?php
/* # Question 3
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
$userInput = "8";
$result = 1;

for ($a = 1; $a < $userInput +1 ; $a++) {
	$result = $result * $a;
		}


echo $result.'<br />';
?>
*/

$userInput = "8";
$result = array();

for ($a = 1; $a < $userInput +1 ; $a++) {

    array_push($result,$a * $a);
}

foreach ($result as $res) {
    echo $res.'<br />';
}


?>
