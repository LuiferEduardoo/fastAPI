from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from .customer import Customer


class InvoiceBase(SQLModel):
    total: int = Field(default=None)


class InvoiceCreate(InvoiceBase):
    customer_id: int


class Invoice(InvoiceBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: Optional[int] = Field(default=None, foreign_key="customer.id")
    customer: Optional[Customer] = Relationship(back_populates="invoices")