from fastapi import FastAPI

import models
from database import engine
from routers import products, orders, payments

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(payments.router)

@app.get("/")
def home():
    return {"message": "Smart Restaurant AI backend funguje"}

