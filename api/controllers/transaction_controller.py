from fastapi import HTTPException
from sqlalchemy.orm import Session
from api.repositories import transaction_repository
from api.schemas.transaction_schema import TransactionCreate, TransactionUpdate, PaymentMethod


def get_all_transactions(db: Session):
    return transaction_repository.get_all_transactions(db)


def get_transaction_by_id(db: Session, transaction_id: int):
    transaction = transaction_repository.get_transaction_by_id(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return transaction


def create_transaction(db: Session, transaction: TransactionCreate):
    return transaction_repository.create_transaction(db, transaction)


def update_transaction(db: Session, transaction_id: int, transaction_data: TransactionUpdate):
    updated = transaction_repository.update_transaction(db, transaction_id, transaction_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return updated


def delete_transaction(db: Session, transaction_id: int):
    deleted = transaction_repository.delete_transaction(db, transaction_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return {"message": "Transação removida com sucesso"}


def get_transactions_by_method(db: Session, method: PaymentMethod):
    return transaction_repository.get_transactions_by_method(db, method)


def get_transactions_by_account(db: Session, account_id: int):
    return transaction_repository.get_transactions_by_account(db, account_id)
