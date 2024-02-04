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
        document.getElementById("assets").textContent="Total Assets = £"+Math.round(data.value*100)/100;


        // statement

        statement = document.getElementById("statement")
        statement.innerHTML = ""


        var income = document.createElement("p")
        a = (Math.round(100*data.balancesheet.income)/100).toFixed(2)
        income.innerText = "Income: + £"+a;
        income.classList.add("pos")
        statement.appendChild(income)

        var income = document.createElement("p")
        b = (Math.round(100*data.balancesheet.tax)/100).toFixed(2)
        income.innerText = "Tax: + £"+b;
        income.classList.add("neg")
        statement.appendChild(income)

        var income = document.createElement("p")
        c = (Math.round(100 * data.balancesheet.expenditures)/100).toFixed(2)
        income.innerText = "Expenditures: + £"+c;
        income.classList.add("neg")
        statement.appendChild(income)

        var income = document.createElement("p")
        income.innerText = "Remaining: + £"+(Math.round(100*(a-b-c))/100).toFixed(2);
        statement.appendChild(income)


        var hr = document.createElement("hr")
        statement.appendChild(hr)

        for (const [key, value] of Object.entries(data.balancesheet.capitalgains)) {
            var income = document.createElement("p")
            income.innerText = key + ":  £"+(Math.round(100*value)/100).toFixed(2);
            statement.appendChild(income)

        }



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

        // set image src
        graphs = document.getElementById("graphs")
        graphs.innerHTML=""
        console.log(Object.entries(data.hint));

        for (const [key, value] of Object.entries(data.graphs)) {
            console.log(key,value)
            var graph = document.createElement('div');
            var name = document.createElement('div');
            name.innerHTML='<b>'+key;
            //name.textContent= key ;
            name.classList.add("graphName")

            var month = document.createElement('span');
            percentChangeMonth = Math.round((value.increasepm-1)*10000)/100;
            textColour = (percentChangeMonth > 0) ? 'pos' : 'neg';
            month.classList.add(textColour);
            month.innerText=percentChangeMonth+"% (Last month)"

            var year = document.createElement('span');
            percentChangeYear = Math.round((value.increasepy-1)*10000)/100;
            textColour = (percentChangeYear > 0) ? 'pos' : 'neg';
            year.classList.add(textColour);
            year.innerText=percentChangeYear+"% (Last year)"

            var img = document.createElement('img');
            img.src = value.graph;
            graph.appendChild(name);
            graph.appendChild(month);
            graph.appendChild(year);
            graph.appendChild(img);
            graphs.appendChild(graph)

        }

        // set tip
        var hint = ""
        for([key,value] of Object.entries(data.hint)){
            hint += value
        }
        document.getElementById("tip").innerHTML = hint;

        updateAssets();

    }).catch(function(err) {
        console.log('Fetch Error :-S', err);
      });

}

function explevel(level){
    fetch("/api/level/"+level).then(function(response) {
        return response.json()
      }).then(updateAssets())
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
            var text2 = document.createTextNode(Math.round(value));
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