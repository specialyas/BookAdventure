from fastapi import FastAPI
from app.models import model
from app.db.session import engine
from app.api.v1.api import api_router


app = FastAPI(
    title="Blog",
    description="This is an api for a blog"
)
#  this is a test comment 

app.include_router(api_router, prefix="/api/v1")

model.Base.metadata.create_all(bind=engine)
