
//7) How to check if two String are Anagram?


<?php
/* Write your PHP code here */
//7) How to check if two String are Anagram?


function anagram($word1, $word2){
    if (strlen($word1) != strlen($word2)){
        echo "they cannot be anagrams as they dont have same length";
    }
    elseif (strtolower($word1) == strtolower($word2))
    {
        echo "they cannot be anagrams as they are the same";
    }
    else {
        $word1Array = str_split($word1);
        $word2Array = str_split($word2);
        sort($word1Array);
        sort($word2Array);
        if (implode('',$word1Array) == implode('',$word2Array)){
            echo "they are anagram";
        }
    }

}

$word1 = "listen";
$word2 = "silent";
/*
$strarray = str_split ($word1);
sort($strarray);
echo implode('', $strarray);
*/
anagram($word1, $word2);
?>
