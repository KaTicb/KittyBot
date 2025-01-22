from aiogram.fsm.state import StatesGroup, State


class WeatherStates(StatesGroup):
    whose_loc = State()
