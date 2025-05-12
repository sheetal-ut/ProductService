from pydantic import BaseModel

class Product(BaseModel):
    product_name: str
    type: str
    brand: str
    price: float
    quantity: int

class ProductResponse(Product):
    product_id: str