from pydantic import BaseModel

class Product(BaseModel):
    id: str | None = None
    name: str
    price: float
    image_url: str
    description: str
    active: bool = True
