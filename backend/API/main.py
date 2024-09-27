from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class UserBase(BaseModel):
    username: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
def read_root(db: db_dependency):
    return {"Hello": "World"}

# @app.post('/posts', status_code=status.HTTP_201_CREATED)
# async def create_post(post: PostBase, db: db_dependency):
#     db_post = models.Post(**post.dict())
#     db.add(db_post)
#     db.commit()
#     return db_post

# @app.get('/posts/{post_id}', status_code=status.HTTP_200_OK)
# async def read_post(post_id: int, db: db_dependency):
#     post = db.query(models.Post).filter(models.Post.id == post_id).first()
#     if post is None:
#         raise HTTPException(status_code=404, detail='Post not found')
#     return post

# @app.delete('/posts/{post_id}', status_code=status.HTTP_200_OK)
# async def delete_post(post_id: int, db: db_dependency):
#     db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=404, detail='Post not found')
#     db.delete(db_post)
#     db.commit()
#     return {"message": "Post deleted"}

# @app.post('/users/', status_code=status.HTTP_201_CREATED)
# async def create_user(user: UserBase, db: db_dependency):
#     db_user = models.User(username=user.username)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# @app.get('/users/{user_id}', status_code=status.HTTP_200_OK)
# async def read_user(user_id: int, db: db_dependency):
#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail='User not found')
#     return user


class MultijatoDataResponse(BaseModel):
    temperatura_entrada_multijato: str
    temperatura_saida_multijato: str

    abertura_valvula_alimentacao: str
    nivel_cozedor: str
    capacitancia_cozedor: str
    pressao_cozedor: str

    abertura_valvula_alimentacao_0: str
    nivel_cozedor_0: str
    capacitancia_cozedor_0: str
    pressao_cozedor_0: str

    abertura_valvula_alimentacao_1: str
    nivel_cozedor_1: str
    capacitancia_cozedor_1: str
    pressao_cozedor_1: str

    abertura_valvula_alimentacao_2: str
    nivel_cozedor_2: str
    capacitancia_cozedor_2: str
    pressao_cozedor_2: str

    abertura_valvula_alimentacao_3: str
    nivel_cozedor_3: str
    capacitancia_cozedor_3: str
    pressao_cozedor_3: str

    abertura_valvula_alimentacao_4: str
    nivel_cozedor_4: str
    capacitancia_cozedor_4: str
    pressao_cozedor_4: str

    abertura_valvula_alimentacao_5: str
    nivel_cozedor_5: str
    capacitancia_cozedor_5: str
    pressao_cozedor_5: str

    abertura_valvula_alimentacao_6: str
    nivel_cozedor_6: str
    capacitancia_cozedor_6: str
    pressao_cozedor_6: str

    class Config:
        orm_mode = True

@app.get('/multijato/', response_model=List[MultijatoDataResponse])
async def get_multijato_data(db: db_dependency):
    data = db.query(models.ProcessData).all()
    if not data:
        raise HTTPException(status_code=404, detail="No data found in process_data table")
    return data
