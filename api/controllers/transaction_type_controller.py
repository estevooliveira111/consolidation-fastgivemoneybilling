from sqlalchemy.orm import Session
from api.repositories import transaction_type_repository
from api.schemas.transaction_type_schema import TransactionTypeCreate, TransactionTypeUpdate


def list_transaction_types(db: Session):
    return transaction_type_repository.get_all_transaction_types(db)


def get_transaction_type(db: Session, type_id: int):
    return transaction_type_repository.get_transaction_type_by_id(db, type_id)


def create_transaction_type(db: Session, type_data: TransactionTypeCreate):
    existing = transaction_type_repository.get_transaction_type_by_name(db, type_data.name)
    if existing:
        raise ValueError("Já existe um tipo de transação com esse nome.")
    return transaction_type_repository.create_transaction_type(db, type_data)


def update_transaction_type(db: Session, type_id: int, type_data: TransactionTypeUpdate):
    return transaction_type_repository.update_transaction_type(db, type_id, type_data)


def delete_transaction_type(db: Session, type_id: int):
    return transaction_type_repository.delete_transaction_type(db, type_id)
