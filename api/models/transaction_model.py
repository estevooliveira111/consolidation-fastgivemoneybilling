from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from api.config.database import Base
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


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True, comment="ID único da transação")
    wallet_id = Column(Integer, ForeignKey("wallets.id"), nullable=False, comment="ID da carteira relacionada")
    type_id = Column(Integer, ForeignKey("transaction_types.id"), nullable=False, comment="ID do tipo de transação")
    account_id = Column(Integer, ForeignKey("bank_accounts.id"), nullable=False, comment="ID da conta bancária associada")
    payment_method = Column(Enum(PaymentMethod), nullable=False, comment="Método de pagamento: pix, boleto, bolepix, card")
    txid = Column(String(128), nullable=True, unique=True, comment="Identificador único da transação (TxID)")
    end_to_end_id = Column(String(128), nullable=True, unique=True, comment="End-to-End ID para rastreamento do pagamento")
    amount = Column(Float, nullable=False, comment="Valor da transação")
    balance = Column(Float, nullable=True, comment="Saldo após a transação (impacto na carteira/conta)")
    description = Column(String(255), nullable=True, comment="Descrição da transação")
    status = Column(Enum(TransactionStatus), default=TransactionStatus.pending, comment="Status da transação: pending, completed, failed")
    payer = Column(JSON, nullable=True, comment="Dados do pagador (nome, documento, banco, agência, conta, tipo de conta, ISPB)")
    receiver = Column(JSON, nullable=True, comment="Dados do recebedor (nome, documento, banco, agência, conta, tipo de conta, ISPB)")
    payment_date = Column(DateTime, nullable=True, comment="Data de pagamento efetiva da transação")
    created_at = Column(DateTime, default=datetime.utcnow, comment="Data de criação do registro")
    event_date = Column(DateTime, nullable=True, comment="Data do evento associado à transação")
    details = Column(JSON, nullable=True, comment="Dados adicionais específicos do método de pagamento (ex: QR code Pix, linha digitável Boleto, parcelas Cartão)")

    wallet = relationship("Wallet", back_populates="transactions")
    type = relationship("TransactionType", back_populates="transactions")
    account = relationship("BankAccount")

