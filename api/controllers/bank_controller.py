from sqlalchemy.orm import Session
from api.repositories import bank_repository
from api.schemas.bank_schema import BankCreate, BankUpdate

def list_banks(db: Session):
    return bank_repository.get_all_banks(db)

def get_bank(db: Session, external_id: int):
    return bank_repository.get_bank_by_external_id(db, external_id)

def create_bank(db: Session, bank: BankCreate):
    return bank_repository.create_bank(db, bank)

def update_bank(db: Session, bank_id: int, bank_data: BankUpdate):
    return bank_repository.update_bank(db, bank_id, bank_data)

def delete_bank(db: Session, bank_id: int):
    return bank_repository.delete_bank(db, bank_id)
