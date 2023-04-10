# Importing necessary modules
from flask import Flask, jsonify, request
import requests
import json
import os
# load_dotenv is a module that loads environment variables from a .env file
from dotenv import load_dotenv
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '''<h2>Welcome to My Weather API Project. Over here you can use the following endpoints</h2>
              <ul>
                <li><strong><em>/weather?city={city_name}</em></strong><br>To get the Current Weather Data of the city whose name you have used.</li><br>
                <li><strong><em>/historical?city={city_name}</em></strong><br>To get the Historical Weather Data of Past 5 Days of the city whose name you have used.</li><br>
                <li><strong><em>/forecast?city={city_name}</em></strong><br>o get the Forecasted Weather Data of Past 5 Days with an interval of 3 Hours.</li>
              </ul>
           '''

@app.route('/weather', methods=['GET'])
def get_weather():
    '''
    `get_weather()` gets the Current Weather Data.
    '''
    # Load environment variables from a .env file
    load_dotenv()
    # Extracting 'city' parameter from the query string
    city = request.args.get('city')
    # Retrieving the API key from environment variables
    api_key = os.getenv("API_KEY")
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)
    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description']
    }
    return jsonify(weather_data)

@app.route('/historical', methods=['GET'])
def get_hweather():
    '''
    `get_hweather()` gets the Historical Weather Data of Past 5 Days.
    '''
    load_dotenv()
    city = request.args.get('city')
    api_key = os.getenv("API_KEY")
    url_current = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response_current = requests.get(url_current)
    data_current = json.loads(response_current.text)
    historical_data = []
    for i in range(1, 5):
        date = datetime.date.today() - datetime.timedelta(days=i)
        timestamp = int(datetime.datetime(date.year, date.month, date.day).timestamp())
        url_historical = f'http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={data_current["coord"]["lat"]}&lon={data_current["coord"]["lon"]}&dt={timestamp}&appid={api_key}&units=metric'
        response_historical = requests.get(url_historical)
        data_historical = json.loads(response_historical.text)
        historical_weather = {
            'date': date.strftime('%Y-%m-%d'),
            'temperature': data_historical["current"]['temp'],
            'humidity': data_historical["current"]['humidity'],
            'description': data_historical["current"]['weather'][0]['description']
        }
        historical_data.append(historical_weather)
    return jsonify(historical_data)

@app.route('/forecast', methods=['GET'])
def get_fweather():
    '''
    `get_fweather()` gets the Forecasted Weather Data of Past 5 Days with an interval of 3 Hours.
    '''
    load_dotenv()
    city = request.args.get('city')
    api_key = os.getenv("API_KEY")
    url_forecast = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response_forecast = requests.get(url_forecast)
    data_forecast = json.loads(response_forecast.text)
    forecast_data = []
    for forecast in data_forecast['list']:
        forecast_weather = {
            'date': forecast['dt_txt'],
            'temperature': forecast['main']['temp'],
            'humidity': forecast['main']['humidity'],
            'description': forecast['weather'][0]['description']
        }
        forecast_data.append(forecast_weather)
    return jsonify(forecast_data)

if __name__ == '__main__':
    app.run(debug=True)
