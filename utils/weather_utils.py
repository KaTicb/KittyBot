from aiohttp import ClientSession
import random

from config import BASE_DIR, settings


async def get_weather(lon, lat) -> dict:

    url = f'http://api.openweathermap.org/data/2.5/weather'
    params = {'lon': lon, 'lat': lat, 'appid': settings.weather_key, 'lang': 'be'}

    async with ClientSession() as session:
        async with session.get(url=url, params=params) as response:
            weather_response = await response.json()
            response = {
                'temp': str(round(weather_response['main']['temp'] - 273.15, 2)),
                'humidity': weather_response['main']['humidity'],


                'description': weather_response['weather'][0]['description'],
                'main_info': weather_response['weather'][0]['main'],

                'country': weather_response['sys']['country'],
                'region_name': weather_response['name'],
            }
            return response


def get_photo_path_by_weather(weather: str) -> str:
    path = BASE_DIR / 'media' / 'img' / weather
    files = list(path.glob('*.jpg'))
    return random.choice(files)
