<?php
/*
Question 5
# Level 1
# Question:
# Define a class which has at least two methods: getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
*/
/*
$userInput = "abcDe Goran";

function getString($userInp){
	echo "User input: <b>".$userInp."</b>";
	printString($userInp);
}

function printString($userInp){
	
	echo " <br/> Before converting to upper case: <b>".$userInp ."</b>.";
	$userInp = strtoupper($userInp);
	echo " <br/> After converting to upper case: <b>".$userInp ."</b>.";
}


getString($userInput);
*/


//the way where i called methods in a static way:
/*
class upperString{
	
	function getString($userInp){
		echo "<br/> User input gotten is: ".$userInp;
		upperString::printString($userInp);
	}
	function printString($userInp){
		//$userInp = strtoupper($userInp);
		echo "<br/> Upper string looks like: ".strtoupper($userInp);
	}
	
}


//calling the method in a static way:
upperString::getString("abcddeeffgg Goran");
*/


class upperString{
	
	function getString($userInp){
		echo "<br/> User input gotten is: ".$userInp;
		
	}
	function printString($userInp){
		//$userInp = strtoupper($userInp);
		echo "<br/> Upper string looks like: ".strtoupper($userInp);
	}
	
}

$first = new upperString();
$first -> getString("abcddeeffgg Goran");
$first -> printString("abcddeeffgg Goran");






?>
