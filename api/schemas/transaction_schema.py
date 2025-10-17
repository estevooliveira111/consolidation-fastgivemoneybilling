from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict
from enum import Enum


class PaymentMethod(str, Enum):
    pix = "pix"
    boleto = "boleto"
    bolepix = "bolepix"
    card = "card"


class TransactionStatus(str, Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"


class PartyInfo(BaseModel):
    name: str
    document: str
    ispb: Optional[str]
    bank: Optional[str]
    agency: Optional[str]
    account: Optional[str]
    account_type: Optional[str]


class TransactionBase(BaseModel):
    wallet_id: int
    type_id: int
    account_id: Optional[int] = None
    payment_method: PaymentMethod
    txid: Optional[str] = None
    end_to_end_id: Optional[str] = None
    amount: float
    balance: Optional[float] = None
    description: Optional[str] = None
    status: Optional[TransactionStatus] = TransactionStatus.pending
    payer: Optional[PartyInfo] = None
    receiver: Optional[PartyInfo] = None
    payment_date: Optional[datetime] = None
    event_date: Optional[datetime] = None
    details: Optional[Dict] = None


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(BaseModel):
    wallet_id: Optional[int]
    type_id: Optional[int]
    account_id: Optional[int]
    payment_method: Optional[PaymentMethod]
    txid: Optional[str]
    end_to_end_id: Optional[str]
    amount: Optional[float]
    balance: Optional[float]
    description: Optional[str]
    status: Optional[TransactionStatus]
    payer: Optional[PartyInfo]
    receiver: Optional[PartyInfo]
    payment_date: Optional[datetime]
    event_date: Optional[datetime]
    details: Optional[Dict]


class TransactionResponse(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
