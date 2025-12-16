from fastapi import FastAPI, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
# from starlette.status import HTTP_201_CREATED

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




@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(blog: schema.Blog, db: Session = Depends(dependencies.get_db)):
    """add a new blog"""
    new_blog = model.Blog(title=blog.title, body=blog.body, )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    # return new_blog
    return {"data": "Blog has been created successfully"}

@app.get("/blog", status_code=200)
def get_blogs(db: Session = Depends(dependencies.get_db)):
    """get all blog post"""
    blogs = db.query(model.Blog).all()
    if not blogs:
        return {"data": "no blogs has been found"}
    return blogs

#
@app.get("/blog/{id}", status_code=200)
def get_blog_by_id(id, response: Response, db: Session = Depends(dependencies.get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:

        raise HTTPException(status_code=404, detail=f"Blog with id ({id}) not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with id {model.Blog.id} not found"}
    return blog


# Code above omitted 👆

# @app.delete("/heroes/{hero_id}")
# def delete_hero(hero_id: int, session: SessionDep):
#     hero = session.get(Hero, hero_id)
#     if not hero:
#         raise HTTPException(status_code=404, detail="Hero not found")
#     session.delete(hero)
#     session.commit()
#     return {"ok": True}

@app.delete("/blog/{blog_id}")
def delete_blog(blog_id, response: Response, db: Session = Depends(dependencies.get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == blog_id).delete(synchronize_session=False)

    # blog = db.get(model.Blog, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog with id ({blog_id}) not found")
    # db.delete(blog)
    db.commit()
    return {"detail": f"Blog with id ({blog_id}) has been deleted successfully"}


@app.put("/blog/{blog_id}")
def update_blog(blog_id, request: schema.Blog,  db: Session = Depends(dependencies.get_db)):
    # blog = db.query(model.Blog).filter(model.Blog.id == blog_id)
    data = db.get(model.Blog, blog_id)
    if not data:
        raise HTTPException(status_code=404, detail=f"Blog with id ({blog_id}) not found")
    data.title = request.title
    data.body = request.body
    data.published_at = request.published_at
    db.add(data)
    db.commit()
    db.refresh(data)
    return {"data": data}

