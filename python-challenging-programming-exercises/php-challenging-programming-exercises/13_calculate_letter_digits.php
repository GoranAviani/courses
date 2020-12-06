<?php
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

$userInput = "hello world! 123";

function calcNum($userInput){
	$numLetters = 0;
	$numNumbers = 0;

	$userInput = str_split($userInput);

	foreach ($userInput as $ui){
		echo $ui;
		echo "<br/>";

		if (ctype_alpha($ui)){
		$numLetters += 1;
		}
		if (ctype_digit($ui)){
		$numNumbers += 1;
		}

	}

	echo "LETTERS ".$numLetters."<br/>";
	echo "DIGITS ". $numNumbers;

	}

calcNum($userInput);



?>
