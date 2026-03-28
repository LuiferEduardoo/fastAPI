from pydantic import BaseModel, EmailStr
from sqlModel import SQLModel


class CustomerBase(SQLModel):
    name: str
    description: str | None
    email: EmailStr
    age: int

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase, table=True):
    id: int | None