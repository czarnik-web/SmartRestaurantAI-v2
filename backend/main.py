from fastapi import FastAPI, HTTPException, Depends


import models
from database import engine, SessionLocal
from routers import products

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(products.router)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Smart Restaurant AI backend funguje"}

