from fastapi import FastAPI
from app.database import get_firestore_client
from routes import products
from routes import orders


app = FastAPI(title="E-Commerce API")

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

app.include_router(products.router)
app.include_router(orders.router)
