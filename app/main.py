from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.routes import register_routers


app = FastAPI(
    title="Blog",
    description="This is an api for a blog"
)
#  this is a test comment 


@app.get('/')
def root():
    return {"message": "Hi from the homepage"}



# app.include_router(api_router, prefix="/api/v1")
# api_router.include_router(posts.router)
# api_router.include_router(users.router)

register_routers(app)

Base.metadata.create_all(bind=engine)
