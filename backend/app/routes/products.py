from fastapi import APIRouter, HTTPException
from app.controllers.product_controller import get_all_products, get_product_by_id

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def list_products():
    return get_all_products()


@router.get("/{product_id}")
def product_details(product_id: str):
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
