__all__ = ('router', )

from aiogram import Router
from .callbacks import router as callback_router

router = Router(name=__name__)
router.include_routers(callback_router,)
