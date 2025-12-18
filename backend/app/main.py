from fastapi import FastAPI
from app.database import get_firestore_client
from app.routes import products
from app.routes import orders
from app.routes import checkout
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="E-Commerce API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    """
    Health check endpoint to verify that:
    - App is running
    - Firestore is reachable
    """
    try:
        db = get_firestore_client()
       
        collections = list(db.collections())
        return {
            "status": "UP",
            "firestore": "CONNECTED",
            "collections_count": len(collections)
        }
    except Exception as e:
        return {
            "status": "DOWN",
            "firestore": "ERROR",
            "error": str(e)
        }

@app.get("/success")
def payment_success():
    return {
        "status": "SUCCESS",
        "message": "Payment completed successfully (Stripe test mode)"
    }

@app.get("/cancel")
def payment_cancel():
    return {
        "status": "CANCELLED",
        "message": "Payment was cancelled"
    }


app.include_router(products.router)
app.include_router(orders.router)
app.include_router(checkout.router)
