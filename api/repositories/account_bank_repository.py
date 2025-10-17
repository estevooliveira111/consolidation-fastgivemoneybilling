from sqlalchemy.orm import Session
from api.models.bank_account_model import BankAccount
from api.schemas.bank_account_schema import BankAccountCreate, BankAccountUpdate

def get_all_bank_accounts(db: Session):
    return db.query(BankAccount).all()

def get_bank_account_by_external_id(db: Session, external_id: str):
    return db.query(BankAccount).filter(BankAccount.external_id == external_id).first()

def create_bank_account(db: Session, account: BankAccountCreate):
    new_account = BankAccount(**account.dict())
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

def update_bank_account(db: Session, external_id: str, account_data: BankAccountUpdate):
    account = db.query(BankAccount).filter(BankAccount.external_id == external_id).first()
    if not account:
        return None
    for key, value in account_data.dict(exclude_unset=True).items():
        setattr(account, key, value)
    db.commit()
    db.refresh(account)
    return account

def delete_bank_account(db: Session, external_id: str):
    account = db.query(BankAccount).filter(BankAccount.external_id == external_id).first()
    if not account:
        return None
    db.delete(account)
    db.commit()
    return account
