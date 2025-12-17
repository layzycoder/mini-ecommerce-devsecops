from app.database import get_firestore_client
from google.cloud.firestore_v1 import SERVER_TIMESTAMP

def create_order(order_data: dict):
    db = get_firestore_client()
    order_data["created_at"] = SERVER_TIMESTAMP

    doc_ref = db.collection("orders").add(order_data)
    return {"message": "Order created successfully", "order_id": doc_ref[1].id}


def get_all_orders():
    db = get_firestore_client()
    orders_ref = db.collection("orders").order_by("created_at", direction="DESCENDING")

    orders = []
    for doc in orders_ref.stream():
        data = doc.to_dict()
        data["id"] = doc.id
        orders.append(data)

    return orders
