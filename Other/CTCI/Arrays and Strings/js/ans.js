//#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
// #cannot use additional data structures?

function unique(word) {
    word = word.split("");
    //console.log(word);
    let result = [];
    let hasIt = false;

    for( let x of word){
		   // console.log(x);

		  if (result.includes(x)){
              hasIt = true;
              break

          } else {
		      result.push(x)
          }

		}

	if (hasIt === true) {
        console.log("duplicates")
    } else {
        console.log("no duplicates")
    }

}


unique("abcdef")

