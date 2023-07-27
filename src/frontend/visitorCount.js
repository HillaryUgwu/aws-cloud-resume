var apiURL = "https://pemsp3t3qg.execute-api.us-east-1.amazonaws.com/dev/guestcount";
fetch(apiURL)
    .then(response => response.json())
    .then(data => {
        document.getElementById('count').innerHTML = data['count']
    })