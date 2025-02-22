from aiogram.fsm.state import StatesGroup, State


class WishStates(StatesGroup):
    base_wish_action_state = State()

    wish_get_list_state = State()
    wish_add_thing_state = State()
    wish_delete_thing_state = State()
    wish_update_thing_state = State()
