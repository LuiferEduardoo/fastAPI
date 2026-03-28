from pydantic import BaseModel
from typing import List
from .customer import Customer
from .transaction import Transaction


class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: List[Transaction]
    total: int 
    
    @property
    def total_amount(self) -> float:
        return sum(transaction.amount for transaction in self.transactions)