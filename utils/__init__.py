__all__ = ('router', )

from aiogram import Router
from .weather_commands import router as weather_router

router = Router(name=__name__)
router.include_router(weather_router)
