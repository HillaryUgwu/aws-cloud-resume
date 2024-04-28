
// import aws from 'https://jspm.dev/aws-sdk';
// const ssm = new aws.SSM();

// async function getApiGatewayEndpoint() {
//   const params = {
//     Name: '/resume/ApiGatewayEndpoint',
//   };

//   const response = await ssm.getParameter(params).promise();
//   return response.Parameter.Value;
// }




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


// // Use the endpoint
// getApiGatewayEndpoint().then(endpoint => {
//     apiURL = endpoint
//     console.log(`API Gateway endpoint: ${endpoint}`);
//   });

// //   let url = await getapi(apiURL, false);
//   let res = await getapi(apiURL, true);