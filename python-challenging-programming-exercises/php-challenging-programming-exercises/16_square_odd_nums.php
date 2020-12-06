<?php
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

$userInput = "1,2,3,4,5,6,7,8,9";

$userInput = explode(",", $userInput);
$resultNormal = array();
$resultSquare = array();

foreach ($userInput as $ui){

	if ($ui % 2 != 0){
		array_push($resultNormal, $ui);
		array_push($resultSquare, $ui*$ui);
	}
}

echo implode(", ", $resultNormal) . " and " . implode(", ", $resultSquare);


?>
