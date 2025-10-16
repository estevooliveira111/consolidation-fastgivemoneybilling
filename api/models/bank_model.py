import uuid
from sqlalchemy import Column, Integer, String
from api.config.database import Base

class Bank(Base):
    __tablename__ = "banks"

    id = Column(
        Integer, 
        primary_key=True, 
        index=True, 
        comment="Identificador único do banco"
    )
    external_id = Column(
        String(36), 
        nullable=False, 
        unique=True, 
        default=lambda: str(uuid.uuid4()), 
        comment="Identificador externo único (UUID gerado automaticamente)"
    )
    name = Column(
        String(255), 
        nullable=False, 
        comment="Nome curto ou sigla do banco"
    )
    full_name = Column(
        String(255), 
        nullable=False, 
        comment="Nome completo do banco"
    )
    code = Column(
        String(20), 
        nullable=False, 
        comment="Código do banco utilizado em sistemas nacionais"
    )
    ispb = Column(
        String(20), 
        nullable=True, 
        comment="Código ISPB do banco (Identificador de Sistema de Pagamentos Brasileiro)"
    )
    country = Column(
        String(2), 
        nullable=False, 
        default="BR", 
        comment="País do banco (padrão BR)"
    )