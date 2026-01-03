
from fastapi import APIRouter
from . import users, posts


routers = [
    users.router,
    posts.router
]


def register_routers(app):
    for router in routers:
        app.include_router(router, prefix="/api/v1")
