from dataclasses import dataclass
from typing import Optional

@dataclass
class Brand:
    value: Optional[str] = None
    text: Optional[str] = None
