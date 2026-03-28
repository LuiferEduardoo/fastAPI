from pydantic import BaseModel


class TransactionBase(BaseModel):
    amount: int
    description: str

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int | None