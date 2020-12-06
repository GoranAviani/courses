<?php
/* Write your PHP code here */
//5) How to find first non repeated character of a given String

function firstNonRep($word){

	for ($i = 0; $i < strlen($word); $i++){
		//echo $word[$i]."<br>";
		if (substr_count($word, $word[$i]) == 1){
			echo "First non repeated word is string is ".$word[$i];
			break;

		}

	}

	/*foreach ($word as $w){
		echo $w;
	}*/

}

$words = "test";
firstNonRep($words);

?>