from fastapi import FastAPI
from app.routes import product_routes

app = FastAPI()

app.include_router(product_routes.router)
