from pydantic import BaseModel, constr, Field, validator
from typing import Optional, Dict, Any
from .bank_schema import BankResponse

class BankAccountBase(BaseModel):
    """Base de dados de uma conta bancária."""
    bank_id: int = Field(..., description="ID do banco ao qual a conta pertence")
    account_number: constr(min_length=1, max_length=50) = Field(..., description="Número da conta bancária")
    account_type: constr(min_length=1, max_length=50) = Field(..., description="Tipo da conta (ex: corrente, poupança)")
    account_name: constr(min_length=1, max_length=255) = Field(..., description="Nome da conta")
    holder_name: constr(min_length=1, max_length=255) = Field(..., description="Nome do titular da conta")
    document: constr(min_length=1, max_length=20) = Field(..., description="Documento do titular (CPF, CNPJ ou passaporte)")
    branch_number: Optional[constr(min_length=1, max_length=20)] = Field(None, description="Número da agência ou filial")
    currency: Optional[constr(min_length=3, max_length=3)] = Field("BRL", description="Moeda da conta (ex: BRL, USD, EUR)")
    country: Optional[constr(min_length=2, max_length=2)] = Field("BR", description="Código ISO do país da conta")
    iban: Optional[constr(min_length=15, max_length=34)] = Field(None, description="Código IBAN para contas internacionais, se aplicável")
    bic_swift: Optional[constr(min_length=8, max_length=11)] = Field(None, description="Código BIC/SWIFT do banco")
    status: Optional[constr(min_length=4, max_length=20)] = Field("active", description="Status da conta (ativo/inativo)")
    extra_data: Optional[Dict[str, Any]] = Field(None, description="Informações adicionais em formato JSON")

    @validator("currency")
    def validate_currency(cls, v):
        allowed = ["BRL", "USD", "EUR"]
        if v not in allowed:
            raise ValueError(f"Moeda inválida. Permitidas: {allowed}")
        return v

    @validator("country")
    def validate_country(cls, v):
        if len(v) != 2:
            raise ValueError("O país deve ser representado pelo código ISO de 2 letras")
        return v.upper()

    @validator("status")
    def validate_status(cls, v):
        allowed = ["active", "inactive"]
        if v not in allowed:
            raise ValueError(f"Status inválido. Permitidos: {allowed}")
        return v


class BankAccountCreate(BankAccountBase):
    """Schema usado para criar uma nova conta bancária."""
    pass


class BankAccountUpdate(BaseModel):
    """Campos que podem ser atualizados em uma conta bancária existente."""
    account_number: Optional[constr(min_length=1, max_length=50)] = Field(None, description="Número da conta bancária")
    account_type: Optional[constr(min_length=1, max_length=50)] = Field(None, description="Tipo da conta (ex: corrente, poupança)")
    holder_name: Optional[constr(min_length=1, max_length=255)] = Field(None, description="Nome do titular da conta")
    branch_number: Optional[constr(min_length=1, max_length=20)] = Field(None, description="Número da agência ou filial")
    currency: Optional[constr(min_length=3, max_length=3)] = Field(None, description="Moeda da conta (ex: BRL, USD, EUR)")
    country: Optional[constr(min_length=2, max_length=2)] = Field(None, description="Código ISO do país da conta")
    status: Optional[constr(min_length=4, max_length=20)] = Field(None, description="Status da conta (ativo/inativo)")
    extra_data: Optional[Dict[str, Any]] = Field(None, description="Informações adicionais em formato JSON")


class BankAccountResponse(BankAccountBase):
    """Schema de resposta de uma conta bancária."""
    id: int = Field(..., description="ID interno da conta")
    external_id: str = Field(..., description="Identificador externo único da conta (UUID)")
    bank: Optional[BankResponse] = Field(None, description="Banco associado à conta")

    class Config:
        from_attributes = True
