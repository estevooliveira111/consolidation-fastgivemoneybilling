import uuid
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from api.config.database import Base

class TransactionType(Base):
    __tablename__ = "transaction_types"

    id = Column(Integer, primary_key=True, index=True, comment="ID interno do tipo de transação")
    external_id = Column(String(36), default=lambda: str(uuid.uuid4()), unique=True, index=True, comment="Identificador externo único (UUID)")

    name = Column(String(100), nullable=False, unique=True, comment="Nome do tipo de transação (ex: PIX_IN)")
    description = Column(String(255), nullable=True, comment="Descrição do tipo de transação")

    status = Column(String(20), default="active", comment="Status do tipo de transação (ativo/inativo)")

    transactions = relationship("Transaction", back_populates="type")