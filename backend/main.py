from fastapi import FastAPI

import models
from database import engine
from routers import products, orders 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
def home():
    return {"message": "Smart Restaurant AI backend funguje"}

