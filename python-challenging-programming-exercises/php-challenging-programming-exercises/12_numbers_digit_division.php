<?php
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
$result = array();

for ($i = 1000; $i < 3001; $i++){
	//echo $i;
	$isEven = true;

	for ($j = 0; $j < strlen(strval($i)); $j++){
		//echo "slovo". strval($i)[$j];

		if (intval(strval($i)[$j]) % 2 != 0){
		$isEven = false;
		}
	}
	if ($isEven == true){
		array_push($result, $i);
	}
	//echo "<br/>";
}
//comment reason: its not specified to display results like bellow:
/*
foreach ($result as $res){
echo $res;
}
*/
echo implode (", ", $result);


?>
