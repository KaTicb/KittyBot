from aiogram import Router, F
from aiogram import types

router = Router(name=__name__)


class BaseCallbacks:
    why_bot = "get_why_bot"
    get_help = "get_help"


@router.callback_query(F.data == BaseCallbacks.why_bot)
async def get_why_bot(callback_query: types.CallbackQuery):
    why_text = """Гэтый бот будзе нашай старонкай кахання, дзе мы зможам сачыць за кожным з нас)\n
    Глядзець надвор'е і мабыць яшчэ функцыі, якія могуць нам спатрэбіцца)))\n"""

    await callback_query.answer(show_alert=True, text=why_text)


@router.callback_query(F.data == BaseCallbacks.get_help)
async def get_help(callback_query: types.CallbackQuery):

    await callback_query.message.answer(text="Націсні -> /help")
