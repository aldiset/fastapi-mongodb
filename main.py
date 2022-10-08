from fastapi import FastAPI
from pymongo import MongoClient

from routes import router as book_router
from config import MONGOHOST, MONGOPORT, MONGONAME

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(host=MONGOHOST, port=MONGOPORT)
    app.database = app.mongodb_client[MONGONAME]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(book_router, tags=["books"], prefix="/book")