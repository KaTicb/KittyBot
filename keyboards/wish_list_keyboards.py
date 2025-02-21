from aiogram.utils.keyboard import ReplyKeyboardBuilder


class WishListButtonKeyboards:
    ADD_TO_LIST = 'Дадаць у ліст'
    REMOVE_FROM_LIST = 'Удаліць з ліста'
    GET_LIST = 'Паказаць ліст'
    UPDATE_LIST = 'Змена ліста'
    CLOSE_WISH_LIST = 'Закрыць ліст'

    ALL = "Усе"
    MY = "Мой ліст"

    @staticmethod
    def wish_list_keyboard():
        keyboard = ReplyKeyboardBuilder()
        keyboard.button(text=WishListButtonKeyboards.ADD_TO_LIST)
        keyboard.button(text=WishListButtonKeyboards.REMOVE_FROM_LIST)
        keyboard.button(text=WishListButtonKeyboards.GET_LIST)
        keyboard.button(text=WishListButtonKeyboards.UPDATE_LIST)
        keyboard.button(text=WishListButtonKeyboards.CLOSE_WISH_LIST)

        keyboard.adjust(2, 2)

        return keyboard.as_markup(resize_keyboard=True)

    @staticmethod
    def get_wish_list_keyboard():
        keyboard = ReplyKeyboardBuilder()
        keyboard.button(text=WishListButtonKeyboards.MY)
        keyboard.button(text=WishListButtonKeyboards.ALL)

        return keyboard.as_markup(resize_keyboard=True)
