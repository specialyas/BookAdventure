from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.dependencies import dependencies
from app.models import model
from app.schemas import schema
from app.database import engine

app = FastAPI(
    title="Blog",
    description="This is an api for a blog"
)


model.Base.metadata.create_all(bind=engine)


@app.get("/")
def index():
    return {"greeting: ""Mr! welcome to the homepage"}




@app.post("/blog")
def create_blog(blog: schema.Blog, db: Session = Depends(dependencies.get_db)):
    new_blog = model.Blog(title=blog.title, body=blog.body, )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


#
# @app.get("/blog/{id}")
# def get_blog_by_id(id: int):
#     return {"data:" [id]}


