
// load AWS SAM Stack Outputs and grab the APIGateway endpoint URL

const apiURL = require('./output.json');
console.log(apiURL[1]['OutputValue']);

// function Func() {
//     fetch("./output.json")
//         .then((res) => {
//             return res.json();
//         })
//         .then((data) => console.log(data));
// }

// fetch("https://juod82fzgl.execute-api.us-east-1.amazonaws.com/Prod/resume/")
//     .then(response => response.json())
//     .then(json => console.log(json));

// $.getJSON("output.json", function (json) {
//     console.log(json); // this will show the info it in firebug console
// });


// var apiURL = "https://pemsp3t3qg.execute-api.us-east-1.amazonaws.com/dev/guestcount";
fetch(apiURL[1]['OutputValue'])
    .then(response => response.json())
    .then(data => {
        document.getElementById('count').innerHTML = data['count']
    })