from pydantic import BaseModel
from typing import Optional

class WalletBase(BaseModel):
    name: str
    balance: float = 0.0
    currency: str = "BRL"
    bank_account_id: Optional[int] = None

class WalletCreate(WalletBase):
    pass

class WalletUpdate(BaseModel):
    name: Optional[str] = None
    balance: Optional[float] = None
    currency: Optional[str] = None
    bank_account_id: Optional[int] = None

class WalletResponse(WalletBase):
    id: int

    class Config:
        orm_mode = True
