
// load AWS SAM Stack Outputs and grab the APIGateway endpoint URL
const apiURL = "./output.json";

// Defining async get api function
async function getapi(url, show) {

    // Storing response
    const response = await fetch(url);

    // Storing data in form of JSON
    var data = await response.json();
    console.log(data);
    if (show) {
        document.getElementById('count').innerHTML = data['count'];
    }
    return data;
}

let url = await getapi(apiURL, false);
let res = await getapi(url[1]["OutputValue"], true);
