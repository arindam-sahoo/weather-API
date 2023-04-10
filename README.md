# Weather API Project
This is a Flask-based API project that retrieves and displays weather data for a specified city. It can display current weather data, historical weather data for the past five days, and forecasted weather data for the next five days with an interval of three hours.

## Prerequisites
- Python 3
- Flask
- requests module
- dotenv module
## Getting Started
1. Clone the repository
2.  Install dependencies using the following command:
    ```
    pip install -r requirements.txt
    ```
3. Create a .env file and add your OpenWeatherMap API key using the following format:
    ```
    API_KEY=<your_api_key>
    ```
4. Run the application using the following command:
    ```
    python app.py
    ```
5. Open a web browser and navigate to http://localhost:5000/ to access the API documentation.
## Usage
### Endpoints
- `/weather?city={city_name}`: To get the current weather data of the specified city.
- `/historical?city={city_name}`: To get the historical weather data of the past five days of the specified city.
- `/forecast?city={city_name}`: To get the forecasted weather data of the next five days with an interval of three hours of the specified city.
### Example
To retrieve the current weather data for London, navigate to `http://localhost:5000/weather?city=London` in a web browser. The API will return a JSON object with the current temperature, humidity, and description.

```json
{
    "city": "London",
    "temperature": 14.11,
    "humidity": 58,
    "description": "clear sky"
}
```

## Attribution
This project uses OpenWeather API and the public API key was used to retrieve weather data.
