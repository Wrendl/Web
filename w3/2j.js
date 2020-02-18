myNodelist = document.getElementsByTagName("LI");
for (i = 0; i < myNodelist.length; i++) {
    var img1 = document.createElement("img");
    img1.src = "https://st2.depositphotos.com/4520249/7735/v/950/depositphotos_77359134-stock-illustration-recycle-bin-icon.jpg";
    img1.className = "close";
    myNodelist[i].appendChild(img1);
}

close = document.getElementsByClassName("close");
for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
            var div = this.parentElement;
            div.style.display = "none";
    }
}

var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
    if (ev.target.tagName === 'LI') {
        ev.target.classList.toggle('checked');
    }
}, false);

function newElement() {
    var li = document.createElement("li");
    var inputValue = document.getElementById("myInput").value;
    var t = document.createTextNode(inputValue);
    li.appendChild(t);
    if (inputValue === '') {
        alert("Write something!");
    } else {
        document.getElementById("myUL").appendChild(li);
    }
    document.getElementById("myInput").value = "";

    
    var img1 = document.createElement("img");
    img1.src = "https://st2.depositphotos.com/4520249/7735/v/950/depositphotos_77359134-stock-illustration-recycle-bin-icon.jpg";
    img1.className = "close";
    myNodelist[i].appendChild(img1);

    for (i = 0; i < close.length; i++) {
        close[i].onclick = function() {
            var div = this.parentElement;
            div.style.display = "none";
        }
    }
}