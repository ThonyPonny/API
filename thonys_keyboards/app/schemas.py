from typing import Optional
from pydantic import BaseModel

class KeyboardBase(BaseModel):
    name: str
    brand: str
    model: str
    switch_type: str
    size: str
    price: float
    rgb: bool = False
    stock: int
    description: Optional[str] = None

class KeyboardCreate(KeyboardBase):
    pass

class KeyboardUpdate(BaseModel):  # Nuevo schema
    name: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    switch_type: Optional[str] = None
    size: Optional[str] = None
    price: Optional[float] = None
    rgb: Optional[bool] = None
    stock: Optional[int] = None
    description: Optional[str] = None

class Keyboard(KeyboardBase):
    id: int
    class Config:
        orm_mode = True