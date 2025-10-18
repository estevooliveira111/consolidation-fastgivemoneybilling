import uuid
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from api.config.database import Base


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True, comment="ID interno da carteira")
    external_id = Column(String(36), default=lambda: str(uuid.uuid4()), unique=True, index=True,
                         comment="Identificador externo único (UUID)")

    name = Column(String(120), nullable=False, comment="Nome da carteira (ex: Carteira Principal)")
    holder_name = Column(String(255), nullable=False, comment="Nome do titular da conta")
    document = Column(String(20), nullable=False, comment="Documento do titular (CPF, CNPJ ou passaporte)")

    status = Column(String(20), nullable=False, default="active", comment="Status da conta (ativo/inativo)")

    fee_pix_in = Column(Float, default=0.0, comment="Taxa cobrada por transação Pix de entrada")
    fee_pix_out = Column(Float, default=0.0, comment="Taxa cobrada por transação Pix de saída")
    fee_boleto = Column(Float, default=0.0, comment="Taxa cobrada por emissão de boleto")
    fee_bolepix = Column(Float, default=0.0, comment="Taxa cobrada por transação BolePix")
    fee_credit_card = Column(Float, default=0.0, comment="Taxa cobrada por transação via cartão de crédito")
    fee_debit_card = Column(Float, default=0.0, comment="Taxa cobrada por transação via cartão de débito")

    balance = Column(Float, default=0.0, comment="Saldo atual da carteira")
    currency = Column(String(10), default="BRL", comment="Moeda associada à carteira")

    transactions = relationship("Transaction", back_populates="wallet")
    bank_account_id = Column(Integer, ForeignKey("bank_accounts.id"), nullable=True, comment="ID da conta bancária associada")
    bank_account = relationship("BankAccount", back_populates="wallets")