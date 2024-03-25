from typing import Optional
from pydantic import BaseModel



class Item(BaseModel):
    name: str
    descriotion: Optional[str] = None
    price: float
    tax: Optional[float] = None
    