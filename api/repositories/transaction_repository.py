from sqlalchemy.orm import Session
from api.models.transaction_model import Transaction
from api.schemas.transaction_schema import TransactionCreate, TransactionUpdate


def get_all_transactions(db: Session):
    return db.query(Transaction).all()


def get_transaction_by_id(db: Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()


def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def update_transaction(db: Session, transaction_id: int, transaction_data: TransactionUpdate):
    db_transaction = get_transaction_by_id(db, transaction_id)
    if not db_transaction:
        return None
    for key, value in transaction_data.dict(exclude_unset=True).items():
        setattr(db_transaction, key, value)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def delete_transaction(db: Session, transaction_id: int):
    db_transaction = get_transaction_by_id(db, transaction_id)
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
    return db_transaction


def get_transactions_by_method(db: Session, method: str):
    return db.query(Transaction).filter(Transaction.payment_method == method).all()


def get_transactions_by_account(db: Session, account_id: int):
    return db.query(Transaction).filter(Transaction.account_id == account_id).all()