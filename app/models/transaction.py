from sqlModel import SQLModel, Field


class TransactionBase(SQLModel):
    amount: int = Field(default=None)
    description: str = Field(default=None)

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)