from sqlalchemy.orm import Session
from api.models.bank_model import Bank
from api.schemas.bank_schema import BankCreate, BankUpdate

def get_all_banks(db: Session):
    return db.query(Bank).all()

def get_bank_by_id(db: Session, bank_id: int):
    return db.query(Bank).filter(Bank.id == bank_id).first()

def get_bank_by_external_id(db: Session, external_id: str):
    return db.query(Bank).filter(Bank.external_id == external_id).first()

def create_bank(db: Session, bank: BankCreate):
    new_bank = Bank(**bank.dict())
    db.add(new_bank)
    db.commit()
    db.refresh(new_bank)
    return new_bank

def update_bank(db: Session, bank_id: int, bank_data: BankUpdate):
    bank = db.query(Bank).filter(Bank.id == bank_id).first()
    if not bank:
        return None
    for key, value in bank_data.dict().items():
        setattr(bank, key, value)
    db.commit()
    db.refresh(bank)
    return bank

def delete_bank(db: Session, bank_id: int):
    bank = db.query(Bank).filter(Bank.id == bank_id).first()
    if not bank:
        return None
    db.delete(bank)
    db.commit()
    return bank
