from aiohttp import ClientSession
import random
import aiosqlite

import json
from datetime import datetime

from config import BASE_DIR

# async def create_table():
#     async with aiosqlite.connect('utils.db') as db:
#         await db.execute('''CREATE TABLE IF NOT EXISTS requests (date DATETIME, city TEXT, utils TEXT)''')
#         await db.commit()


# async def save_to_db(city, utils):
#     async with aiosqlite.connect('utils.db') as db:
#
#         query = '''INSERT INTO requests (date, city, utils) VALUES (?, ?, ?)'''
#
#         try:
#             await db.execute(query, (datetime.now(), city, json.dumps(utils)))
#         except aiosqlite.Error as e:
#             print(f"Ошибка при выполнении запроса: {e}")
#
#         await db.commit()


async def get_weather(lon, lat) -> dict:

    url = f'http://api.openweathermap.org/data/2.5/weather'
    params = {'lon': lon, 'lat': lat, 'appid': '2a4ff86f9aaa70041ec8e82db64abf56', 'lang': 'be'}

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
