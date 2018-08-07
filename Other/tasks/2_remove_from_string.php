//2) Write a method which will remove any given character from a String?

<?php
/* Write your PHP code here */
//2) Write a method which will remove any given character from a String?

$word = "removaaaae a aaaa letaateraaa";
$letter = "a";
function removal($word, $letter){
	$result = "";
	//$word = str_split($word);

	//echo is_array($word) ? 'it is an array' : 'not an Array';



	for ($i = 0; $i < strlen($word); $i++){
		//echo $word[$i]." <br\> ";

		if ($word[$i] != $letter){
			//echo $word[$i];
			$result .= $word[$i];
		}

	}

	echo $result;
}

removal($word, $letter);
?>
