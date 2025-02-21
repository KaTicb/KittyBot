from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown

from keyboards.base_keyboards import BaseButtonKeyboards, InlineBaseButtonKeyboards

router = Router(name=__name__)


@router.message(CommandStart())
async def start_command(message: types.Message):
    text = """Прывітанне! Гэта <b>"Кацянятны бот"</b>. І тут ёсць... кісімісі мяў мяў мяў)\n
    Кацянятны бот яшчэ не дароблен. Гэта першая версія.\n"""
    await message.answer(text=text, reply_markup=InlineBaseButtonKeyboards.get_start_keyboard())


@router.message(F.text == BaseButtonKeyboards.HELP)
@router.message(Command('help'))
async def help_command(message: types.Message):
    text = markdown.text("/start - Прывітанне\n"
                         "/help - Дапамога\n"
                         "/weather - Надвор'е\n"
                         "/wish_list - Ліст жаданняў\n"
                         )
    await message.answer(text=text)
