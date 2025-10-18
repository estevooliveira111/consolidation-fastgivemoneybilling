import uuid
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from api.config.database import Base
from api.models.bank_account_model import BankAccount

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String(36), default=lambda: str(uuid.uuid4()), unique=True, index=True)
    name = Column(String(120), nullable=False)
    holder_name = Column(String(255), nullable=False)
    document = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False, default="active")

    fee_pix_in = Column(Float, default=0.0)
    fee_pix_out = Column(Float, default=0.0)
    fee_boleto = Column(Float, default=0.0)
    fee_bolepix = Column(Float, default=0.0)
    fee_credit_card = Column(Float, default=0.0)
    fee_debit_card = Column(Float, default=0.0)

    balance = Column(Float, default=0.0)
    currency = Column(String(10), default="BRL")

    transactions = relationship("TransactionModel", back_populates="wallet")
    
    bank_account_id = Column(Integer, ForeignKey("bank_accounts.id"), nullable=True)
    bank_account = relationship(BankAccount, back_populates="wallets")