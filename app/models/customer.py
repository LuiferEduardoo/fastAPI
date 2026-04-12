from pydantic import EmailStr
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .invoice import Invoice


class CustomerBase(SQLModel):
    name: str = Field(default=None)
    description: Optional[str] = Field(default=None)
    email: EmailStr = Field(default=None)
    age: int = Field(default=None)

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    invoices: List["Invoice"] = Relationship(back_populates="customer")