from pydantic import BaseModel


class Transaction(BaseModel):
    id: int
    ammount: int
    description: str