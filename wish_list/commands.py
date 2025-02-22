from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.enums import ChatAction
from aiogram.utils.chat_action import ChatActionSender
from aiogram.fsm.context import FSMContext

from .model import DatabaseManager
from .states import WishStates

from keyboards.wish_list_keyboards import WishListButtonKeyboards
from aiogram.types import ReplyKeyboardRemove

import typing

router = Router(name=__name__)


# Base commands
@router.message(Command("wish_list") or WishStates.base_wish_action_state)
async def wish_list_command(message: types.Message, state: FSMContext):
    await state.set_state(WishStates.base_wish_action_state)

    async with ChatActionSender(
            bot=message.bot,
            chat_id=message.chat.id,
            action=ChatAction.TYPING
    ):
        await message.answer(text="Выберы дзеянне:", reply_markup=WishListButtonKeyboards.wish_list_keyboard())


# Get list commands
@router.message(WishStates.base_wish_action_state, F.text == WishListButtonKeyboards.GET_LIST)
async def get_list_command(message: types.Message, state: FSMContext):
    await state.set_state(WishStates.wish_get_list_state)

    async with ChatActionSender(
            bot=message.bot,
            chat_id=message.chat.id,
            action=ChatAction.TYPING
    ):
        await message.answer(text="Напішы імя чалавека, чый ліст жаданняў хочаш убачыць, альбо напішы сябе:",
                             reply_markup=WishListButtonKeyboards.get_wish_list_keyboard())


def get_text_from_db(wish_list: typing.Iterable) -> str:
    username = None
    text = ""
    for item in wish_list:
        if item[1] != username:
            username = item[1]
            text += f"<b>{username}</b>\n"

        text += f"<b>-</b> <i>{item[2][:11]}</i> {item[3]}   <b>Нумар</b>: {item[0]};\n\n"
    return text


# need feature
@router.message(WishStates.wish_get_list_state)
async def get_list_command_whose(message: types.Message, state: FSMContext):
    await state.set_state(WishStates.base_wish_action_state)
    database = DatabaseManager()
    if message.text == WishListButtonKeyboards.MY:
        wish_list = await database.get_list_by_owner(message.from_user.username)
    elif message.text == WishListButtonKeyboards.ALL:
        wish_list = await database.get_all_list()
    else:
        wish_list = await database.get_list_by_owner(message.text)

    text = get_text_from_db(wish_list)

    await message.answer(text=text, reply_markup=WishListButtonKeyboards.wish_list_keyboard())


# Add to list commands
@router.message(WishStates.base_wish_action_state, F.text == WishListButtonKeyboards.ADD_TO_LIST)
async def add_list_command(message: types.Message, state: FSMContext):
    await state.set_state(WishStates.wish_add_thing_state)
    await message.answer(text="Напішы жаданне:", reply_markup=ReplyKeyboardRemove())


@router.message(WishStates.wish_add_thing_state)
async def add_item_list_command(message: types.Message, state: FSMContext):
    await state.set_state(WishStates.base_wish_action_state)
    username = message.from_user.username
    database = DatabaseManager()

    await database.create_item(message.text, username)
    await message.answer(text="Жаданне дададзена! Яшчэ жадання?",
                         reply_markup=WishListButtonKeyboards.wish_list_keyboard())


# Delete from list commands
@router.message(WishStates.base_wish_action_state, F.text == WishListButtonKeyboards.REMOVE_FROM_LIST)
async def delete_list_command(message: types.Message, state: FSMContext):
    await state.set_state(WishStates.wish_delete_thing_state)

    database = DatabaseManager()
    wish_list = await database.get_list_by_owner(message.from_user.username)
    text = get_text_from_db(wish_list)
    text += "Напішы <b>нумар рэчы</b>, якую хочаш выдаліць:"

    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())


@router.message(WishStates.wish_delete_thing_state)
async def add_item_list_command(message: types.Message, state: FSMContext):
    await state.set_state(WishStates.base_wish_action_state)

    database = DatabaseManager()
    try:
        item_id = int(message.text)
        if item_id < 1:
            raise ValueError

        await database.delete_item(item_id)
        await message.answer(text="Рэч выдалена паспяхова!", reply_markup=WishListButtonKeyboards.wish_list_keyboard())

    except ValueError:
        await state.set_state(WishStates.wish_delete_thing_state)
        await message.answer(text="Нумар з літар або з сімвалаў! Павінны быць лічбы болей нуля (1)!")

    # except something from DB:


# Close state command
@router.message(WishStates.base_wish_action_state, F.text == WishListButtonKeyboards.CLOSE_WISH_LIST)
async def close_list_command(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(text="Ліст жаданняў закрыты!", reply_markup=ReplyKeyboardRemove())
