<?php
/*
# Question 18
# Level 3
# Question:
# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
*/


$userInput = "ABd1234@1,a F1#,2w3E*,2We3345";

function checkPassword($userInput){
	$result = array();
	//echo $userInput;
	$userInput = explode(",", $userInput);
	//echo $userInput;



	foreach ($userInput as $ui){
		echo "<br/><br/>*length: ".strlen($ui)."<br/>";
		$hasLowerLetter = false;
		$hasUpperLetter = false;
		$hasNumber = false;
		$hasCharacter = false;
		$hasLength = false;

		echo "####password: ".$ui."<br/>";

		if ((strlen($ui) > 5) and (strlen($ui) < 13)){
			$hasLength = true;
			echo "#velicina je dobra <br/>";
		}

		for ($i = 0; $i < strlen($ui) ; $i++){
			echo "Pass char: ". $ui[$i]."<br/>";


			//if it is a letter
			if (ctype_alpha($ui[$i])){
				if (ctype_upper($ui[$i])){
					$hasUpperLetter = true;
					echo "#ima veliko <br/>";
				}
				if (ctype_lower($ui[$i])){
					$hasLowerLetter = true;
					echo "#ima malo <br/>";
				}
			}

			if (is_numeric($ui[$i])){
				$hasNumber = true;
				echo "#ima broj <br/>";
			}

			if (preg_match('/[\'^£$%&*()}{@#~?><>,|=_+¬-]/', $ui[$i]))
				{
					$hasCharacter = true;
					echo "#has special <br/>";
				}
		}

		if (( $hasLowerLetter == true) and ($hasUpperLetter == true) and ($hasNumber == true) and 	($hasCharacter == true) and ($hasLength == true)){
			echo "<br/><br/> its ok : ".$ui;
			array_push($result, $ui);

		}

	}
	echo "<br/><br/>final results are: ".json_encode($result);



}


checkPassword($userInput);
?>