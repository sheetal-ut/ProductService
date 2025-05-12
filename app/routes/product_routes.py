from fastapi import APIRouter, HTTPException
from typing import List
from app.models.product import Product, ProductResponse
from app.db.mongo import collection
from fastapi import UploadFile, File
import pandas as pd
import uuid

router = APIRouter()

def product_to_response(product) -> ProductResponse:
    return ProductResponse(
        product_id=str(product["_id"]),  # Use MongoDB _id as product_id
        product_name=product["product_name"],
        type=product["type"],
        brand=product["brand"],
        price=product["price"],
        quantity=product["quantity"]
    )

@router.get("/products", response_model=List[ProductResponse])
async def get_products():
    cursor = collection.find()
    products = await cursor.to_list(length=100)
    return [product_to_response(p) for p in products]

@router.post("/products", response_model=ProductResponse)
async def create_product(product: Product):
    product_dict = product.dict()  # Convert Pydantic model to dictionary
    res = await collection.insert_one(product_dict)  # MongoDB generates _id
    created = await collection.find_one({"_id": res.inserted_id})
    return product_to_response(created)

@router.post("/import-excel")
async def import_excel(file: UploadFile = File(...)):
    # Read the uploaded Excel file
    contents = await file.read()
    df = pd.read_excel(contents, engine="openpyxl")

    # Validate required columns
    required_columns = {"product_name", "type", "brand", "price", "quantity"}
    if not required_columns.issubset(df.columns):
        raise HTTPException(status_code=400, detail=f"Missing required columns: {required_columns - set(df.columns)}")

    # Convert DataFrame rows to product dicts
    products = []
    for _, row in df.iterrows():
        product = {
            "product_name": row["product_name"],
            "type": row["type"],
            "brand": row["brand"],
            "price": float(row["price"]),
            "quantity": int(row["quantity"]),
        }
        products.append(product)

    # Bulk insert into MongoDB
    result = await collection.insert_many(products)
    return {"message": f"{len(result.inserted_ids)} products imported successfully"}
