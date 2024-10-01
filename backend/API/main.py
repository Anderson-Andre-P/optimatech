from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

models.Base.metadata.create_all(bind=engine)

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

class MultijatoDataResponse(BaseModel):
    tempo: datetime
    temperatura_entrada_multijato: float
    temperatura_saida_multijato: float

    abertura_valvula_alimentacao: float
    nivel_cozedor: float
    capacitancia_cozedor: float
    pressao_cozedor: float

    abertura_valvula_alimentacao_0: float
    nivel_cozedor_0: float
    capacitancia_cozedor_0: float
    pressao_cozedor_0: float

    abertura_valvula_alimentacao_1: float
    nivel_cozedor_1: float
    capacitancia_cozedor_1: float
    pressao_cozedor_1: float

    abertura_valvula_alimentacao_2: float
    nivel_cozedor_2: float
    capacitancia_cozedor_2: float
    pressao_cozedor_2: float

    abertura_valvula_alimentacao_3: float
    nivel_cozedor_3: float
    capacitancia_cozedor_3: float
    pressao_cozedor_3: float

    abertura_valvula_alimentacao_4: float
    nivel_cozedor_4: float
    capacitancia_cozedor_4: float
    pressao_cozedor_4: float

    abertura_valvula_alimentacao_5: float
    nivel_cozedor_5: float
    capacitancia_cozedor_5: float
    pressao_cozedor_5: float

    abertura_valvula_alimentacao_6: float
    nivel_cozedor_6: float
    capacitancia_cozedor_6: float
    pressao_cozedor_6: float

    class Config:
        orm_mode = True

@app.get('/multijato/', response_model=List[MultijatoDataResponse])
async def get_multijato_data(db: db_dependency):
    data = db.query(models.ProcessData).all()
    if not data:
        raise HTTPException(status_code=404, detail="No data found in process_data table")
    return data
