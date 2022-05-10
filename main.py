from typing import Optional, List
from uuid import uuid4
from fastapi import FastAPI
from pydantic import BaseModel
from models import User, Gender, Role, Product

      
app = FastAPI()
db_1: List[User] = [
    User(id=uuid4(), 
        first_name="Anh",
        last_name="Nguyen",
        gender= Gender.female,
        roles=[Role.admin, Role.user],
        is_active=True
        )
        ]

db_2: List[Product] = [
        Product(id=1,
            ProductName='Painting',
            ProductID=uuid4(),
            Price= 200.00,
            Ship_time=None,
            Decription='5 point'       
            )
    ]



@app.get("/api/users/v1")
async def users():
    return db_1;

@app.get("/api/users/v2")
async def product():
    return db_2;

@app.post("/api/users/v3")
async def product():
    return db_2;