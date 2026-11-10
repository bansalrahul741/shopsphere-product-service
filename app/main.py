from fastapi import FastAPI

from app.database import Base, engine
from app.models.product import Product
from app.routes import products

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ShopSphere Product Service",
    description="Product catalogue microservice",
    version="1.0.0"
)

app.include_router(
    products.router,
    prefix="/products",
    tags=["Products"]
)


@app.get("/")
def root():
    return {
        "message": "Welcome to ShopSphere Product Service",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}