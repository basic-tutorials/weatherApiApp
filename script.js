document.getElementById('location-form').addEventListener('submit', async function(event) {
  event.preventDefault();
  const location = document.getElementById('location-input').value;
  const weatherData = await getWeatherData(location);
  displayWeatherInfo(weatherData);
});

async function getWeatherData(location) {
  const apiKey = 'YOUR_WEATHERAPI_KEY';
  const apiUrl = `http://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${location}&aqi=no`;
  const response = await fetch(apiUrl);
  const data = await response.json();
  return data;
}

function displayWeatherInfo(weatherData) {
  const weatherInfoElement = document.getElementById('weather-info');
  weatherInfoElement.innerHTML = `
    <h2>${weatherData.location.name}</h2>
    <p>Temperature: ${weatherData.current.temp_c}°C</p>
    <p>Condition: ${weatherData.current.condition.text}</p>
    <p>Wind Speed: ${weatherData.current.wind_kph} km/h</p>
    <p>Humidity: ${weatherData.current.humidity}%</p>
    <p>Cloud Cover: ${weatherData.current.cloud}%</p>
  `;
}
