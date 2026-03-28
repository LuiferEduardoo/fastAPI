from sqlModel import SQLModel


class TransactionBase(SQLModel):
    amount: int
    description: str

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase, table=True):
    id: int | None