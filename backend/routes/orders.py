from fastapi import APIRouter, HTTPException
from controllers.order_controller import create_order, get_all_orders

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/")
def place_order(order: dict):
    if not order.get("items"):
        raise HTTPException(status_code=400, detail="Order items required")

    return create_order(order)


@router.get("/")
def list_orders():
    return get_all_orders()
