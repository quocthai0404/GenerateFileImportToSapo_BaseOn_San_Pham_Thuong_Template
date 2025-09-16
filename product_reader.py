import json
from typing import List
from models.product import Product
from models.unit import Unit
from models.brand import Brand


def _normalize_brand(b):
    if b is None:
        return None
    if isinstance(b, dict):
        return Brand(value=b.get('value'), text=b.get('text'))
    return b  # string


def _normalize_images(img):
    # JSON sometimes has images as string or array; return string or list
    if img is None:
        return None
    return img


def load_products(file_path: str) -> List[Product]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    products: List[Product] = []

    for p in data.get("data", []):
        # parse units
        units = []
        for u in p.get("units", []):
            brand = _normalize_brand(u.get("brand"))
            unit_kwargs = {**u}
            unit_kwargs["brand"] = brand
            # ensure keys exist
            units.append(Unit(**unit_kwargs))

        prod_kwargs = {**p}
        prod_kwargs["units"] = units
        prod_kwargs["images"] = _normalize_images(p.get("images"))
        prod_kwargs["brand"] = _normalize_brand(p.get("brand"))

        products.append(Product(**prod_kwargs))

    return products
