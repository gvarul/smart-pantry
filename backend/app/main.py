from fastapi import FastAPI
from .database import engine, Base
from .api import items, usage, shopping, notifications
from .tasks import start_scheduler
from . import models

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Pantry API")

app.include_router(items.router)
app.include_router(usage.router)
app.include_router(shopping.router)
app.include_router(notifications.router)

@app.on_event("startup")
def on_startup():
    start_scheduler()

@app.get("/")
def root():
    return {"msg": "Smart Pantry API up"}
