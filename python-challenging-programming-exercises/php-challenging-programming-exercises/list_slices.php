<?php
/*
#Question:
#Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.
#Hints:
#Use ** operator to get power of a number.
#Use range() for loops.
#Use list.append() to add values into a list.
#Use [n1:n2] to slice a list
*/

$result = array();

for ($i = 0; $i < 21; $i++){
array_push($result, $i * $i);
}
/*
foreach($result as $res){
echo $res;
echo "<br/>";
}
*/
$slicedResult =( array_slice($result,1,5));

foreach($slicedResult as $res){
echo $res;
echo "<br/>";
}

?>
