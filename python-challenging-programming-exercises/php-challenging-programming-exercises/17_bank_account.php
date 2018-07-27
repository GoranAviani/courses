<?php
/*
# Question 17
# Level 2
# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. T
# he transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
*/

//Since its PHP I will send commands as an argument in a array of strings.
function banking ($userInput){
	$balance = 0;
	
	/*
	//just checking the function argumet
	foreach ($userInput as $ui){
	echo $ui;
	echo "<br/>";
	}
	*/
	for ($i = 0; $i < count($userInput); $i ++){
		//echo $userInput[$i];
		$ui = explode(" ",$userInput[$i]);
		
		// $j < 1 because input has only 2 parts, command and number
		for ($j = 0; $j < 1; $j++){
			echo "first part: ".$ui[0]."<br/>";
			echo "second part: ".$ui[1]."<br/>";
		
			if ($ui[0] == "D"){
				$balance += $ui[1];
			}
			
			if ($ui[0] == "W"){
				$balance -= $ui[1];
			}
		
		
			
		}
		
	echo "Bank balance is: " .$balance ."<br/>";
			
	}
	
	
	
	
}


$userInput = array("D 300", "D 300", "W 200", "D 100");
banking($userInput);

?>
