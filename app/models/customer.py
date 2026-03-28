from pydantic import BaseModel, EmailStr
from typing import Optional


class Customer(BaseModel):
    name: str
    description: str
    email: EmailStr
    age: int
