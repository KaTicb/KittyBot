__all__ = ('router', )

from aiogram import Router
from .commands import router as base_router

router = Router(name=__name__)
router.include_router(base_router)
