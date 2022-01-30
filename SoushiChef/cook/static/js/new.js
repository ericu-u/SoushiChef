
bt = document.getElementById("bt")
bt.addEventListener("click", function(){
    var msg = new SpeechSynthesisUtterance();
    msg.text = "Fuck garlic my bro throw that shit away";
    window.speechSynthesis.speak(msg);

    console.log("here")
}, false);