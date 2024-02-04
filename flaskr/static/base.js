// document.getElementById("clickMe").onclick = function () { alert('hello!'); };

function loads(){
    nextmonth()
}

function nextmonth() {
    // alert(1)
    fetch("/api/nextmonth").then(function(response) {
        return response.json()
      }).then(function(data) {
        age = 18 + Math.floor(data.time / 12)
        months = data.time % 12
        document.getElementById("age").textContent=age+"y "+months+"m";
        document.getElementById("assets").textContent="£"+Math.round(data.value*100)/100;

        // setnews

        stories = document.getElementById("stories")
        stories.innerHTML=""


        for (const [key, value] of Object.entries(data.news)) {
            console.log(key,value)
            var story = document.createElement('div');
            story.classList.add("story")
            var h3 = document.createElement('h3');
            var text1 = document.createTextNode(key);
            var p = document.createElement('p');
            var text2 = document.createTextNode(value);

            h3.appendChild(text1);
            p.appendChild(text2);
            story.appendChild(h3);
            story.appendChild(p);

            stories.appendChild(story);
        }


        updateAssets();

    }).catch(function(err) {
        console.log('Fetch Error :-S', err);
      });

}

function buy(assetname){
    value = document.getElementById("buy"+assetname).value;
    fetch("/api/buy/"+assetname+"/"+value).then(function(response) {
        return response.json()
      }).then(updateAssets())
}
function sell(assetname){
    value = document.getElementById("sell"+assetname).value;
    fetch("/api/sell/"+assetname+"/"+value).then(function(response) {
        return response.json()
      }).then(updateAssets())
}

function updateAssets(){
    fetch("/api/getassets").then(function(response) {
        return response.json()
      }).then(function(data) {
        table = document.getElementById("assettable");
        table.innerHTML = "<tr><th>Name</th><th>Value</th><th>Buy</th><th>Sell</th></tr>";
        for (const [key, value] of Object.entries(data)) {
            var tr = document.createElement('tr');

            var td1 = document.createElement('td');
            var text1 = document.createTextNode(key);
            var td2 = document.createElement('td');
            var text2 = document.createTextNode(value);
            // var td3 = document.createElement('td');
            // td3.innerHTML = "?"
            var td4 = document.createElement('td');
            td4.innerHTML = "<input type=\"number\" id=\"buy"+key+"\" name=\"name\" /><button onclick=\"buy('"+key+"')\">Buy</button>"
            var td5 = document.createElement('td');
            td5.innerHTML = "<input type=\"number\" id=\"sell"+key+"\"/><button onclick=\"sell('"+key+"')\">Sell</button>"


            td1.appendChild(text1);
            td2.appendChild(text2);
            tr.appendChild(td1);
            tr.appendChild(td2);
            // tr.appendChild(td3);
            if (key!="savings"){
                tr.appendChild(td4);
                tr.appendChild(td5);

            }

            table.appendChild(tr);
        }


    }).catch(function(err) {
        console.log('Fetch Error :-S', err);
      });

}