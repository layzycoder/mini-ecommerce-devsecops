from app.database import get_firestore_client

products = [
    {
        "name": "Wireless Mouse",
        "price": 25.99,
        "image_url": "https://via.placeholder.com/150",
        "description": "Ergonomic wireless mouse",
        "active": True
    },
    {
        "name": "Keyboard",
        "price": 45.99,
        "image_url": "https://via.placeholder.com/150",
        "description": "RGB mechanical keyboard",
        "active": True
    }
]

def add():
    db = get_firestore_client()
    for product in products:
        db.collection("products").add(product)
    print("Products added successfully")

if __name__ == "__main__":
    add()
