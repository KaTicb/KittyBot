from aiogram import Router, types, F
from aiogram.enums import ChatAction
from aiogram.utils.chat_action import ChatActionSender
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

import config

from .states import WeatherStates
from . import weather_utils
from keyboards.weather_keyboards import *

router = Router(name=__name__)


@router.message(Command("weather"))
async def weather_start_command(message: types.Message, state: FSMContext):
    text = """Выберы дзеянне:"""

    await state.set_state(WeatherStates.whose_loc)

    await message.answer_photo(
        photo=types.FSInputFile(
            path=config.WEATHER_BASE_PHOTO_PATH
        ),
        caption=text,
        reply_markup=WeatherButtonKeyboards.get_wheather_start_keyboard()
    )


@router.message(WeatherStates.whose_loc, F.location)
async def weather_command(message: types.Message, state: FSMContext):

    await state.clear()

    async with ChatActionSender(
        bot=message.bot,
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    ):
        lon = message.location.longitude
        lat = message.location.latitude
        weather = await weather_utils.get_weather(lon, lat)
        text = f"Сучаснае надвор'е ў <b>{weather['country']}, {weather['region_name']}</b>: {weather['temp']} °C\n" \
               f"Даўгата: {lon}°, Шырыня: {lat}°\n" \
               f"Вільготнасць: {weather['humidity']}%\n" \
               f"Зараз <b>{weather['description']}!</b>"

        await message.answer_photo(
            photo=types.FSInputFile(
                path=weather_utils.get_photo_path_by_weather(weather['main_info']),
            ),
            caption=text,
            reply_markup=ReplyKeyboardRemove()
        )
