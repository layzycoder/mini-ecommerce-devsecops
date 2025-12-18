from app.database import get_firestore_client
from app.models.product import Product

def get_all_products():
    db = get_firestore_client()
    products_ref = db.collection("products").where("active", "==", True)

    products = []
    for doc in products_ref.stream():
        data = doc.to_dict()
        data["id"] = doc.id
        products.append(data)

    return products


def get_product_by_id(product_id: str):
    db = get_firestore_client()
    doc_ref = db.collection("products").document(product_id)
    doc = doc_ref.get()

    if not doc.exists:
        return None

    data = doc.to_dict()
    data["id"] = doc.id
    return data
