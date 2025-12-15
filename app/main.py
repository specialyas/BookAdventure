from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

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




@app.post("/blog", status_code=HTTP_201_CREATED)
def create_blog(blog: schema.Blog, db: Session = Depends(dependencies.get_db)):
    """add a new blog"""
    new_blog = model.Blog(title=blog.title, body=blog.body, )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog", status_code=200)
def get_blogs(db: Session = Depends(dependencies.get_db)):
    """get all blog post"""
    blogs = db.query(model.Blog).all()
    return blogs

#
@app.get("/blog/{id}")
def get_blog_by_id(id, db: Session = Depends(dependencies.get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    return blog


