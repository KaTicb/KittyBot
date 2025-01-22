from aiogram.utils.keyboard import ReplyKeyboardBuilder


class WeatherButtonKeyboards:
    GET_WEATHER_FOR_VASYA = "Сучаснае надвор'е ў Кісі!"
    GET_WEATHER_FOR_KIRYL = "Сучаснае надвор'е ў Місі!"

    @staticmethod
    def get_wheather_start_keyboard():
        keyboard = ReplyKeyboardBuilder()
        keyboard.button(text="Тваё сучаснае надвор'е :)", request_location=True)
        keyboard.button(text=WeatherButtonKeyboards.GET_WEATHER_FOR_KIRYL)
        keyboard.button(text=WeatherButtonKeyboards.GET_WEATHER_FOR_VASYA)

        keyboard.adjust(1, 2)

        return keyboard.as_markup(
            resize_keyboard=True,
            input_field_placeholder="Что зрабіць?",
        )
