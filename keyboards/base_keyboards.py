from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from .weather_keyboards import WeatherButtonKeyboards
from .callbacks import BaseCallbacks


class BaseButtonKeyboards:
    HELP = "Дапамога па боту"

    @staticmethod
    def get_base_keyboard():
        keyboard = ReplyKeyboardBuilder()

        keyboard.add(types.KeyboardButton(text=BaseButtonKeyboards.HELP))
        keyboard.add(types.KeyboardButton(text=WeatherButtonKeyboards.GET_WEATHER_FOR_VASYA, request_location=True))
        keyboard.add(types.KeyboardButton(text=WeatherButtonKeyboards.GET_WEATHER_FOR_KIRYL, request_location=True))

        keyboard.adjust(1, 2)

        return keyboard.as_markup(resize_keyboard=True)


class InlineBaseButtonKeyboards:
    WHY = "Навошта гэты бот?"
    HELP = "Дапамога па боту, альбо паглядзець каманды."
    MOVE_TO_DEV = "Перайсці на старонку распрацоўніка бота (Місі)"

    @staticmethod
    def get_start_keyboard():
        keyboard = InlineKeyboardBuilder()
        keyboard.add(
            types.InlineKeyboardButton(text=InlineBaseButtonKeyboards.WHY, callback_data=BaseCallbacks.why_bot))
        keyboard.add(
            types.InlineKeyboardButton(text=InlineBaseButtonKeyboards.HELP, callback_data=BaseCallbacks.get_help))
        keyboard.add(
            types.InlineKeyboardButton(text=InlineBaseButtonKeyboards.MOVE_TO_DEV, url='https://t.me/kikijuly3'))

        keyboard.adjust(1, 1)

        return keyboard.as_markup()
