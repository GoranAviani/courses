<?php
/* Write your PHP code here */
//6) How to count occurrence of a given character in a String?


function occur1($word, $letter){
    echo substr_count($word, $letter);

    $numOccur = 0;
    for ($i = 0; $i < strlen($word); $i++){
        if ($word[$i] == $letter){
            $numOccur +=1;
        }
    }
    echo $numOccur;

    $numOccur = 0;
    $word = str_split($word);
    foreach ($word as $w){
        if ($w == $letter){
            $numOccur += 1;
        }
    }

    echo $numOccur;

}

$words = "test tt t";
$letter = "t";
occur1($words, $letter);

?>
