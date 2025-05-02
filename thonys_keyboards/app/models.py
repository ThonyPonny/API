from .database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean

class Keyboard(Base):
    __tablename__ = "keyboards"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    brand = Column(String(50))
    model = Column(String(50))
    switch_type = Column(String(30))
    size = Column(String(20))
    price = Column(Float)
    rgb = Column(Boolean, default=False)
    stock = Column(Integer)
    description = Column(String(500))