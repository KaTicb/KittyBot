__all__ = ('router', )

from aiogram import Router
from .commands import router as wish_list_router

router = Router(name=__name__)
router.include_router(wish_list_router)