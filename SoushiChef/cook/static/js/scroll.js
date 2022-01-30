// Pre-determiend scroll height
let pageHeight = window.innerHeight;

// Initial Start page
start = document.getElementById("st-bt")
start.addEventListener("click", function(){
    window.scrollBy(0, pageHeight);
}, false);

// Nav buttons
back = document.getElementById('back')
back.addEventListener("click", function(){
    window.scrollBy(0, -pageHeight);
}, false);

front = document.getElementById('forward')
front.addEventListener("click", function(){
    window.scrollBy(0, pageHeight);
}, false);

// Style
licon = document.getElementById('iback')
ricon = document.getElementById('iforward')
front.addEventListener("mouseover", function(){
    ricon.style.opacity = "1"
}, false);
back.addEventListener("mouseover", function(){
    licon.style.opacity = "1"
}, false);

front.addEventListener("mouseleave", function(){
    ricon.style.opacity = "0"
}, false);
back.addEventListener("mouseleave", function(){
    licon.style.opacity = "0"
}, false);