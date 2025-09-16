from dataclasses import dataclass, field
from typing import List, Optional, Union
from .unit import Unit
from .brand import Brand

@dataclass
class Product:
    id: Optional[int] = None
    price: Optional[int] = None
    sku: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    alias: Optional[str] = None
    product_type: Optional[str] = None
    position: Optional[int] = None
    total_sell: Optional[int] = None
    country: Optional[str] = None
    rating: Optional[int] = None
    tags: List[str] = field(default_factory=list)
    price_promotion: Optional[int] = None
    product_id: Optional[int] = None
    selling_price: Optional[int] = None
    units: List[Unit] = field(default_factory=list)
    images: Optional[Union[str, List[str]]] = None
    # brand can be a simple string or an object {value,text}
    brand: Optional[Union[str, Brand]] = None
    # Additional optional fields commonly present in JSON exports
    content: Optional[str] = None
    categories: Optional[str] = None
    main_image: Optional[Union[str, List[str]]] = None
    url: Optional[str] = None
    summary: Optional[str] = None
