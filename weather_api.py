import requests
from logging_util import get_logger

logger = get_logger()

API_KEY = "your_openweathermap_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(location):
    try:
        params = {"q": location, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"The weather in {location} is {weather} with a temperature of {temp}°C."
    except requests.exceptions.RequestException as e:
        logger.exception(f"Error fetching weather: {e}")
        return "Could not fetch the weather data right now."
