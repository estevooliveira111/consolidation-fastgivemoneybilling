from pydantic import BaseModel, constr
from typing import Optional

class BankBase(BaseModel):
    name: constr(max_length=255)
    full_name: constr(max_length=255)
    code: constr(max_length=20)
    ispb: Optional[constr(max_length=20)] = None
    country: Optional[constr(max_length=2)] = "BR"

class BankCreate(BankBase):
    class Config:
        from_attributes = True

class BankUpdate(BaseModel):
    name: Optional[constr(max_length=255)] = None
    full_name: Optional[constr(max_length=255)] = None
    code: Optional[constr(max_length=20)] = None
    ispb: Optional[constr(max_length=20)] = None
    country: Optional[constr(max_length=2)] = None

    class Config:
        from_attributes = True

class BankResponse(BankBase):
    id: int
    external_id: str

    class Config:
        from_attributes = True
