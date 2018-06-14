const testWrapper = document.querySelector(".test-wrapper");
const testArea = document.querySelector("#test-area");
const originText = document.querySelector("#origin-text p").innerHTML;
const resetButton = document.querySelector("#reset");
const theTimer = document.querySelector(".timer");

 let timer = 0;
// Add leading zero to numbers 9 or below (purely for aesthetics):


// Run a standard minute/second/hundredths timer:

function runTimer(){
    theTimer.innerHTML = timer ;
    timer++;

}


// Match the text entered with the provided text on the page:
function spellCheck(){
    let textEntered = testArea.value.length;

    console.log(textEntered)
}

// Start the timer:
function startTimer(){
    let textEnteredLength = testArea.value.length;
    console.log(textEnteredLength)

    //When the first key is pressed start the timer runTimer
    if (textEnteredLength === 0){
        setInterval(runTimer,10);
    }

}

// Reset everything:
function resetText() {
    console.log("Reset btn is pressed");
}

// Event listeners for keyboard input and the reset button:
testArea.addEventListener("keypress",startTimer,false);
testArea.addEventListener("keyup", spellCheck, false);
resetButton.addEventListener("click", resetText, false);