from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional, Dict
from enum import Enum
from sqlalchemy.orm import Session

from api.config.database import SessionLocal
from api.models.wallet_model import Wallet
from api.models.transaction_type_model import TransactionType
from api.models.bank_account_model import BankAccount

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
    wallet_id: Optional[int]
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

    @validator("wallet_id")
    def validate_wallet_exists(cls, v):
        db: Session = SessionLocal()
        wallet = db.query(Wallet).filter(Wallet.id == v).first()
        db.close()
        if not wallet:
            raise ValueError(f"Wallet com id={v} não encontrada")
        return v

    @validator("type_id")
    def validate_type_exists(cls, v):
        db: Session = SessionLocal()
        tx_type = db.query(TransactionType).filter(TransactionType.id == v).first()
        db.close()
        if not tx_type:
            raise ValueError(f"TransactionType com id={v} não encontrado")
        return v

    @validator("account_id")
    def validate_account_exists(cls, v):
        if v is None:
            return v
        db: Session = SessionLocal()
        account = db.query(BankAccount).filter(BankAccount.id == v).first()
        db.close()
        if not account:
            raise ValueError(f"BankAccount com id={v} não encontrado")
        return v


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
        from_attributes = True
