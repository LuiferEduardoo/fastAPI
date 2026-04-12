from sqlmodel import SQLModel, Field
from typing import Optional


class TransactionBase(SQLModel):
    amount: int = Field(default=None)
    description: str = Field(default=None)

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)