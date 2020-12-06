<?php
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
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
*/


$userInput = "3,5";

function twoDArray($userInput){
	$result = array();
	$userInput = explode(',', $userInput);


		for ($i=0; $i < $userInput[0]; $i++){
			//echo $i;
			$tempArray = array();
			for ($j=0; $j < $userInput[1]; $j++){

				array_push($tempArray,$i * $j);
				//echo "<br/>brojevi su ".$i * $j;
			}

			foreach ($tempArray as $ta){
			//echo "<br/>temp array je ".$ta;
			}
			array_push($result, $tempArray);
		}

	foreach ($result as $res){
		echo "<br/>";
		echo implode(",",$res);
	}


}

twoDArray($userInput);
?>


