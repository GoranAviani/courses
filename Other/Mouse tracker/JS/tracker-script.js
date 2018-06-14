const AREA = document.body;
const CIRCLE = document.querySelector('.circle');
const CIRCLE2 = document.querySelector('.circle2');

const windowWidth = window.innerWidth;
const windowHeight = window.innerHeight;

function mouseCoordinates(e) {
    // Capture the event object (mouse movement).
    // Get X coordinate (distance from left viewport edge) via clientX property.
    // Take total window width, subtract current coordinate and width of circle.
    // Do the same for Y coordinate (distance from top viewport edge).
    let horizontalPosition = windowWidth - e.clientX +26;
    let verticalPosition= windowHeight - e.clientY + 26;

   //To follow mouse
    //let horizontalPosition = e.clientX - 26;
    //let verticalPosition= e.clientY -26;

    // Set horizontal and vertical position.
    CIRCLE2.style.left = horizontalPosition +50+ 'px';
    CIRCLE2.style.top = verticalPosition +-75+ 'px';
    CIRCLE.style.left = horizontalPosition + 'px';
    CIRCLE.style.top = verticalPosition + 'px';

}

function changeColorOnTouch() {
    CIRCLE.style.backgroundColor = "green";
    CIRCLE.style.borderColor = "green";

}

function changeColorOnTouch2() {
    CIRCLE2.style.backgroundColor = "red";
    CIRCLE2.style.borderColor = "red";
}

// When the mouse moves, run the mouseCoordinates function.
AREA.addEventListener('mousemove', mouseCoordinates, false);

// When the mouse touches the circle, run the changeColorOnTouch function.
CIRCLE.addEventListener('mouseenter', changeColorOnTouch, false);
CIRCLE2.addEventListener('mouseenter', changeColorOnTouch2, false);

// When the mouse leaves the circle, remove inline styles with an anonymous function.
CIRCLE.addEventListener('mouseleave', function(){CIRCLE.removeAttribute("style");}, false);
CIRCLE2.addEventListener('mouseleave', function(){CIRCLE2.removeAttribute("style");}, false);