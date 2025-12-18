from fastapi import APIRouter, HTTPException
import stripe
from app.security import get_stripe_secret_key

router = APIRouter(prefix="/checkout", tags=["Checkout"])

stripe.api_key = get_stripe_secret_key()

@router.post("/")
def create_checkout_session(order: dict):
    try:
        line_items = []

        for item in order.get("items", []):
            line_items.append({
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item["name"],
                    },
                    "unit_amount": int(item["price"] * 100),
                },
                "quantity": item["quantity"],
            })

        if not line_items:
            raise HTTPException(status_code=400, detail="No items in order")

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url="http://127.0.0.1:8000/success",
            cancel_url="http://127.0.0.1:8000/cancel",
        )

        return {
            "checkout_url": session.url
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
