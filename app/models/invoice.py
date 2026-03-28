from pydantic import BaseModel
from sqlModel import SQLModel, Field

from typing import List
from .customer import Customer
from .transaction import Transaction


class InvoiceBase(SQLModel):
    customer: Customer
    transactions: List[Transaction]
    total: int = Field(default=None)
    
    @property
    def total_amount(self) -> float:
        return sum(transaction.amount for transaction in self.transactions)

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase, table=True):
    id: int | None = Field(default=None, primary_key=True)