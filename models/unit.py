from dataclasses import dataclass, field
from typing import Optional, Union
from .brand import Brand

@dataclass
class Unit:
    variant_unit_name: Optional[str] = None
    convert_variant_unit: Optional[int] = None
    inventory_quantity: Optional[int] = None
    variant_id: Optional[int] = None
    price_promotion: Optional[int] = None
    main_image: Optional[Union[str, list]] = None
    selling_price: Optional[int] = None
    show_unit_image: Optional[bool] = None
    show_unit_name: Optional[bool] = None
    sku: Optional[str] = None
    title: Optional[str] = None
    name: Optional[str] = None
    brand: Optional[Union[Brand, str]] = None  # May be dict or string
