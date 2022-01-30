
// For adding event listenrs to return data-name
var btn = document.getElementsByClassName("favbtn");
for (var i = 0; i < btn.length; i++) {
    var thisBtn = btn[i];
    thisBtn.addEventListener("click", function(){
        $.ajax({
            type: 'POST',
            url: "/post/ajax/favorite",
            data: {
                "name": this.dataset.name,
                "sp": '{{ sp }}'
            },
            success: function (response) {
                location.href="/menu"
            },
            error: function (response) {
                console.log("fail")
            }
        })
    }, false);
}
