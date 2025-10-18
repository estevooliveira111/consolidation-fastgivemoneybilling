from pydantic import BaseModel
from typing import Optional

class TransactionTypeBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: str = "active"


class TransactionTypeCreate(TransactionTypeBase):
    pass


class TransactionTypeUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


class TransactionTypeResponse(TransactionTypeBase):
    id: int
    external_id: str

    class Config:
        from_attributes = True
