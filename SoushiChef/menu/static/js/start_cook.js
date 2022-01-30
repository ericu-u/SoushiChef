
// For adding event listenrs to return data-name
var btn = document.getElementsByClassName("cookbtn");
for (var i = 0; i < btn.length; i++) {
    var thisBtn = btn[i];
    thisBtn.addEventListener("click", function(){
        $.ajax({
            type: 'POST',
            url: "/post/ajax/route_cook",
            data: {
                "name": this.dataset.name,
                "sp": '{{ sp }}'
            },
            success: function (response) {
                console.log("FINSIHED!@")
                location.href="/cook"
            },
            error: function (response) {
                console.log("fail")
            }
        })
    }, false);
}

