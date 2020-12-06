/*for ($a = 2000; $a < 3021; $a++) {
	if (($a % 7 == 0) and ($a %5 != 0)){
		echo "Value of a : ". $a ."<br/>";
	}
    
}
*/


$result = array();

for ($a = 2000; $a < 3021; $a++) {
	if (($a % 7 == 0) and ($a %5 != 0)){
		array_push($result,$a);
	}    
}

foreach ($result as $res) {
echo $res.'<br />';
}