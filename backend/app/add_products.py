from app.database import get_firestore_client

products = [
    {
        "name": "Lenovo ThinkPad T490",
        "price": 1099,
        "image_url": "https://storage.googleapis.com/mini-ecommerce-products/ThinkPadT490.jpg",
        "description": "Lenovo ThinkPad series laptops win-11, 14inch screen, touch, 8GB, 256GB",
        "active": True
    },
    {
        "name": "ThinkPad P16",
        "price": 989,
        "image_url": "https://storage.googleapis.com/mini-ecommerce-products/ThinkPad_P16.jpg",
        "description": "2024 P16 Lenovo ThinkPad series- 16GB, 256GB, windows-10Pro",
        "active": True
    },
    {
        "name": "Lenovo ThinkPad Gen12 X1 laptop",
        "price": 1579,
        "image_url": "https://storage.googleapis.com/mini-ecommerce-products/ThinkpadGen12X1.jpg",
        "description": "Gen 12 X1 Carbon, Windows 11(Pro), 32GB RAM, 1TB SSD, Intel graphics",
        "active": True
    },
    {
        "name": "Thinkpad_Bussiness laptops",
        "price": 1398,
        "image_url": "https://storage.googleapis.com/mini-ecommerce-products/Thinkpad_Bussiness.jpg",
        "description": "16B RAM, 512 SSD, Windows 11, Touch screen, Intel Core i7",
        "active": True
    },
    {
        "name": "Thinkpad T series laptops - T480",
        "price": 1055,
        "image_url": "https://storage.googleapis.com/mini-ecommerce-products/Thinkpad_T480.jpg",
        "description": "Lenovo Thinkpad T moel laptops - Win-11, 256SSD, 8GB, NVIDIA Graphic card",
        "active": True
    },
    {
        "name": "Lenovo ThinkPad YOGA series-260",
        "price": 699,
        "image_url": "https://storage.googleapis.com/mini-ecommerce-products/Thinkpad_Yoga_260.jpg",
        "description": "ThinkPad Yoga series laptops, 512SSD, 8GB, Windows-11",
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
