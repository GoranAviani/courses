//1) Write code to check a String is palindrome or not?



<?php
/* Write your PHP code here */
function palindrome($word){
	if ($word == strrev($word)){
		echo $word ." is a palindrome";}
	else{
	echo $word ." is not a palindrome";
	}
}



palindrome("madama");

?>
