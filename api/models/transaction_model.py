from sqlalchemy import Column, Integer, Float, String, ForeignKey, Enum, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from api.config.database import Base
from api.models.wallet_model import Wallet
from api.models.transaction_type_model import TransactionType
from api.models.bank_account_model import BankAccount
import enum

class PaymentMethod(str, enum.Enum):
    pix = "pix"
    boleto = "boleto"
    bolepix = "bolepix"
    card = "card"

class TransactionStatus(str, enum.Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"

class TransactionModel(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    wallet_id = Column(Integer, ForeignKey("wallets.id"), nullable=True)
    type_id = Column(Integer, ForeignKey("transaction_types.id"), nullable=False)
    account_id = Column(Integer, ForeignKey("bank_accounts.id"), nullable=False)
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    txid = Column(String(128), nullable=True, unique=True)
    end_to_end_id = Column(String(128), nullable=True, unique=True)
    amount = Column(Float, nullable=False)
    balance = Column(Float, nullable=True)
    description = Column(String(255), nullable=True)
    status = Column(Enum(TransactionStatus), default=TransactionStatus.pending)
    payer = Column(JSON, nullable=True)
    receiver = Column(JSON, nullable=True)
    payment_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    event_date = Column(DateTime, nullable=True)
    details = Column(JSON, nullable=True)

    wallet = relationship(Wallet, back_populates="transactions")
    type = relationship(TransactionType, back_populates="transactions")
    account = relationship(BankAccount)
