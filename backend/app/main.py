from fastapi import FastAPI
from app.database import get_firestore_client
from app.routes import products
from app.routes import orders
from app.routes import checkout
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os


app = FastAPI(title="E-Commerce API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(BASE_DIR, "web")

app.mount("/css", StaticFiles(directory=os.path.join(WEB_DIR, "css")), name="css")
app.mount("/js", StaticFiles(directory=os.path.join(WEB_DIR, "js")), name="js")

images_dir = os.path.join(WEB_DIR, "images")
if os.path.isdir(images_dir):
    app.mount("/images", StaticFiles(directory=images_dir), name="images")

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


# Pages
@app.get("/")
def serve_home():
    return FileResponse(os.path.join(WEB_DIR, "index.html"))

@app.get("/products.html")
def serve_products_page():
    return FileResponse(os.path.join(WEB_DIR, "products.html"))

@app.get("/product.html")
def serve_product_page():
    return FileResponse(os.path.join(WEB_DIR, "product.html"))

@app.get("/cart.html")
def serve_cart_page():
    return FileResponse(os.path.join(WEB_DIR, "cart.html"))

@app.get("/admin.html")
def serve_admin_page():
    return FileResponse(os.path.join(WEB_DIR, "admin.html"))