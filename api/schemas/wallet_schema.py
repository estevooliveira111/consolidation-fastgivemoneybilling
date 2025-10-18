from pydantic import BaseModel, Field, constr
from .bank_schema import BankResponse
from typing import Optional
from datetime import datetime

class WalletBase(BaseModel):
    name: constr(min_length=1, max_length=120)
    holder_name: constr(min_length=1, max_length=255)
    document: constr(min_length=1, max_length=20)
    status: Optional[constr(min_length=4, max_length=20)] = "active"
    
    fee_pix_in: Optional[float] = 0.0
    fee_pix_out: Optional[float] = 0.0
    fee_boleto: Optional[float] = 0.0
    fee_bolepix: Optional[float] = 0.0
    fee_credit_card: Optional[float] = 0.0
    fee_debit_card: Optional[float] = 0.0
    
    currency: Optional[constr(min_length=3, max_length=10)] = "BRL"
    bank_account_id: Optional[int]


class WalletCreate(WalletBase):
    pass

class WalletUpdate(BaseModel):
    name: Optional[str] = None
    balance: Optional[float] = None
    currency: Optional[str] = None
    bank_account_id: Optional[int] = None

class WalletResponse(WalletBase):
    id: int = Field(..., description="ID interno da carteira")
    external_id: str = Field(..., description="UUID externo da carteira")
    balance: float = Field(..., description="Saldo atual da carteira")

    class Config:
        from_attributes = True
