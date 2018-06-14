const testWrapper = document.querySelector(".test-wrapper");
const testArea = document.querySelector("#test-area");
const originText = document.querySelector("#origin-text p").innerHTML;
const resetButton = document.querySelector("#reset");
const theTimer = document.querySelector(".timer");

    //minutes, seconds, hundrens of seconds, thousends of seconds
 let timer = [0,0,0,0];

// Add leading zero to numbers 9 or below (purely for aesthetics):
function leadingZero(time){
    //If it is a single digit number add 0 in front
    if (time <= 9){
    time = "0" + time;
    }
    return time
}

// Run a standard minute/second/hundredths timer:

function runTimer(){

    let currentTime = leadingZero(timer[0])+":"+leadingZero(timer[1])+":"+leadingZero(timer[2])

    theTimer.innerHTML = currentTime ;
    timer[3]++;



    //minutes dividing by 100 to get seconds, and dividing by 60 to get minutes
    timer[0] = Math.floor((timer[3]/100/60))

    // - timer[0] * 60 = every time it hits 60 seconds this value returns to zero
    timer[1] = Math.floor((timer[3]/100) - (timer[0] * 60))

    // - timer[1] * 100 = every time it hits 100 part of a second it goes to 0
    //every time a minute reach a hundred so it does not count over
    timer[2] = Math.floor((timer[3] - timer[1] * 100 ) - (timer[0] * 6000))



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