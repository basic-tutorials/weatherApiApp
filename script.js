function getWeather() {
    var location = document.getElementById("location").value;
    var apiKey = "4516173a2e8d4123969121246241302";
    var url = "https://api.weatherapi.com/v1/current.json?key=" + apiKey + "&q=" + location;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            displayWeather(data);
        })
        .catch(error => {
            console.log("Error:", error);
        });
}

function displayWeather(data) {
    var weatherData = document.getElementById("weather-data");
    if (data.error) {
        weatherData.textContent = "Error: " + data.error.message;
    } else {
        var location = data.location.name + ", " + data.location.country;
        var condition = data.current.condition.text;
        var temperature = data.current.temp_c + "°C";
        var humidity = "Humidity: " + data.current.humidity + "%";
        var windSpeed = "Wind Speed: " + data.current.wind_kph + " km/h";

        weatherData.innerHTML = "<strong>Location:</strong> " + location + "<br>" +
                                "<strong>Condition:</strong> " + condition + "<br>" +
                                "<strong>Temperature:</strong> " + temperature + "<br>" +
                                humidity + "<br>" +
                                windSpeed;
    }
}
