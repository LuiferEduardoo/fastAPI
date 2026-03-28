from pydantic import BaseModel
from typing import List
from .customer import Customer
from .transaction import Transaction


class InvoiceBase(BaseModel):
    customer: Customer
    transactions: List[Transaction]
    total: int 
    
    @property
    def total_amount(self) -> float:
        return sum(transaction.amount for transaction in self.transactions)

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int | None