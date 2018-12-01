
function addData(){

    var name = document.getElementById("name").value;
    var price = document.getElementById("price").value;
    var description = document.getElementById("description").value;
    var color = document.getElementById("color").value;
    let url = document.getElementById("url").value;

    // var data = JSON.stringify({
    //     "name": "iphone 11",
    //     "price": 500000,
    //     "description": "This is an awesome phone...",
    //     "color": "RED",
    //     "url": "https://images-na.ssl-images-amazon.com/images/I/71x3e0x%2BM2L._SL1382_.jpg"
    // });

    var data = JSON.stringify({
        "name": name,
        "price": price,
        "description": description,
        "color": color,
        "url": url
    });

    var xhr = new XMLHttpRequest();

    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            console.log(this.responseText);
            document.getElementById("data").innerHTML = this.responseText;
        }
    });


    xhr.open("POST", "/product");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.send(data);
}
