<?php
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

$userInput = "Hello world!";

function calcUppLow($userInput){
	$uppLetters = 0;
	$lowLetters = 0;

	$userInput = str_split($userInput);

	foreach ($userInput as $ui){
		echo $ui;
		echo "<br/>";

		if (ctype_alpha($ui)){
			if (ctype_upper($ui)){
			$uppLetters += 1;
			}
			if (ctype_lower($ui)){
			$lowLetters += 1;
		}


		}

	}

	echo "UPPER CASE ". $uppLetters."<br/>";
	echo "LOWER CASE ". $lowLetters;

	}

calcUppLow($userInput);



?>
