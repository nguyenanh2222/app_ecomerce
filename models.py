from datetime import datetime
from decimal import Decimal
from typing import Optional, List
from uuid import uuid4, UUID
from pydantic import BaseModel
from enum import Enum


class Product(BaseModel):
    id: int
    ProductName: str
    ProductID: Optional[UUID]
    Price: Decimal
    Ship_time: Optional[datetime] = None
    Decription: str

class Gender(str, Enum):
    male ='male'
    female = 'female'
    
class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    
class User(BaseModel):
    ID: Optional[UUID] = uuid4
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]
    is_active: bool