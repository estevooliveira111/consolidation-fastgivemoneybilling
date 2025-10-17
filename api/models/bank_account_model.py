from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON, Float
from sqlalchemy.orm import relationship
from api.config.database import Base
import uuid
from datetime import datetime

class BankAccount(Base):
    __tablename__ = "bank_accounts"

    id = Column(Integer, primary_key=True, index=True, comment="ID interno da conta bancária")
    external_id = Column(String(36), default=lambda: str(uuid.uuid4()), unique=True, index=True, comment="Identificador externo único (UUID)")
    bank_id = Column(Integer, ForeignKey("banks.id"), nullable=False, comment="ID do banco ao qual a conta pertence")
    account_number = Column(String(50), nullable=False, comment="Número da conta bancária")
    account_type = Column(String(50), nullable=False, comment="Tipo da conta (ex: corrente, poupança)")
    account_name = Column(String(255), nullable=False, comment="Nome da conta")
    holder_name = Column(String(255), nullable=False, comment="Nome do titular da conta")
    document = Column(String(20), nullable=False, comment="Documento do titular (CPF, CNPJ ou passaporte)")
    branch_number = Column(String(20), nullable=True, comment="Número da agência ou filial")
    currency = Column(String(3), nullable=False, default="BRL", comment="Moeda da conta (ex: BRL, USD, EUR)")
    country = Column(String(2), nullable=False, default="BR", comment="Código ISO do país da conta")
    iban = Column(String(34), nullable=True, comment="Código IBAN para contas internacionais, se aplicável")
    bic_swift = Column(String(11), nullable=True, comment="Código BIC/SWIFT do banco")
    status = Column(String(20), nullable=False, default="active", comment="Status da conta (ativo/inativo)")
    extra_data = Column(JSON, nullable=True, comment="Metadados adicionais da conta")

    cost_boleto = Column(Float, nullable=True, comment="Custo por emissão de boleto simples")
    cost_boleto_hybrid = Column(Float, nullable=True, comment="Custo por emissão de boleto híbrido")
    cost_pix_in = Column(Float, nullable=True, comment="Custo para recebimento via Pix")
    cost_pix_out = Column(Float, nullable=True, comment="Custo para envio via Pix")

    created_at = Column(DateTime, default=datetime.utcnow, comment="Data de criação do registro")
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment="Data da última atualização do registro")

    bank = relationship("Bank", backref="accounts")
    wallets = relationship("Wallet", back_populates="bank_account")
