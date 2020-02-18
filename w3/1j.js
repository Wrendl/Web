let box = document.querySelector('.items');
let input = document.querySelector('.inp');
let btn = document.querySelector('.button1');

List = document.getElementsByTagName("label");
for(i=0; i<List.length; i++){
    
}



function addElement(){
    let new_btn = document.createElement("input");
    new_btn.type = "checkbox";
    new_btn.className = "open";
    let new_el = document.createElement("label");
    new_el.innerHTML = input.value;
    new_el.className = "open";
    let img1 = document.createElement("img");
    img1.onclick = "deleteElement()";
    img1.className = "open";
    img1.src = "https://st2.depositphotos.com/4520249/7735/v/950/depositphotos_77359134-stock-illustration-recycle-bin-icon.jpg";
    let brr = document.createElement("br");
    brr.className = "open";
    let pp = document.createElement("p");
    pp.className = "open";
    if ( input.value === '' ){
        alert("Write Something!");
    }else{
        box.appendChild(new_btn);
        box.appendChild(new_el);
        box.appendChild(img1);
        box.appendChild(brr);
        box.appendChild(pp);

        input.value = "";
    }
}
function deleteElement(){

}