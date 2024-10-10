import requests
import os

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city):
    """
    Получает текущую погоду для указанного города с
    использованием API OpenWeatherMap.
    """
    # api_key = '6b65e9ce77f9ebd587d7173e325139d5'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
