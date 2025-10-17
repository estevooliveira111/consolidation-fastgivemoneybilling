from sqlalchemy.orm import Session
from api.models.transaction_type_model import TransactionType
from api.schemas.transaction_type_schema import TransactionTypeCreate, TransactionTypeUpdate


def get_all_transaction_types(db: Session):
    return db.query(TransactionType).all()


def get_transaction_type_by_id(db: Session, type_id: int):
    return db.query(TransactionType).filter(TransactionType.id == type_id).first()


def get_transaction_type_by_name(db: Session, name: str):
    return db.query(TransactionType).filter(TransactionType.name == name).first()


def create_transaction_type(db: Session, type_data: TransactionTypeCreate):
    new_type = TransactionType(**type_data.dict())
    db.add(new_type)
    db.commit()
    db.refresh(new_type)
    return new_type


def update_transaction_type(db: Session, type_id: int, type_data: TransactionTypeUpdate):
    transaction_type = get_transaction_type_by_id(db, type_id)
    if not transaction_type:
        return None

    for key, value in type_data.dict(exclude_unset=True).items():
        setattr(transaction_type, key, value)

    db.commit()
    db.refresh(transaction_type)
    return transaction_type


def delete_transaction_type(db: Session, type_id: int):
    transaction_type = get_transaction_type_by_id(db, type_id)
    if not transaction_type:
        return None
    db.delete(transaction_type)
    db.commit()
    return transaction_type
