from fastapi import APIRouter, HTTPException, Depends
from app.controllers.order_controller import create_order, get_all_orders
from app.auth import verify_admin


router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/")
def place_order(order: dict):
    if not order.get("items"):
        raise HTTPException(status_code=400, detail="Order items required")

    return create_order(order)


# @router.get("/")
# def list_orders():
#     return get_all_orders()

@router.get("/", dependencies=[Depends(verify_admin)])
def list_orders():
    return get_all_orders()
