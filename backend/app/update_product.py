from app.database import get_firestore_client

# Map: product name -> new image url
IMAGE_UPDATES = {
    "Wireless Mouse": "https://storage.googleapis.com/mini-ecommerce-products/mouse.jpg",
    "Keyboard": "https://storage.googleapis.com/mini-ecommerce-products/keyboard.jpg",
    # "USB-C Hub": "https://picsum.photos/seed/hub/600/400",
    # "Noise Cancelling Headphones": "https://picsum.photos/seed/headphones/600/400",
    # "Laptop Stand": "https://picsum.photos/seed/stand/600/400",
    # "Webcam": "https://picsum.photos/seed/webcam/600/400",
}

def main():
    db = get_firestore_client()
    products_ref = db.collection("products")

    updated = 0
    for name, url in IMAGE_UPDATES.items():
        docs = products_ref.where("name", "==", name).stream()
        found = False
        for doc in docs:
            products_ref.document(doc.id).set({"image_url": url}, merge=True)
            updated += 1
            found = True
            print(f"Updated {name} (doc_id={doc.id})")
        if not found:
            print(f"Not found by name: {name}")

    print(f"\nDone. Updated {updated} document(s).")

if __name__ == "__main__":
    main()
