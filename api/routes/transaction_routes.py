from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.config.database import get_db
from api.controllers import transaction_controller
from api.schemas.transaction_schema import TransactionCreate, TransactionUpdate, TransactionResponse, PaymentMethod

router = APIRouter(prefix="/transactions", tags=["Transações"])


@router.get("/", response_model=List[TransactionResponse])
def list_transactions(db: Session = Depends(get_db)):
    return transaction_controller.get_all_transactions(db)


@router.get("/method/{method}", response_model=List[TransactionResponse])
def list_transactions_by_method(method: PaymentMethod, db: Session = Depends(get_db)):
    return transaction_controller.get_transactions_by_method(db, method)


@router.get("/account/{account_id}", response_model=List[TransactionResponse])
def list_transactions_by_account(account_id: int, db: Session = Depends(get_db)):
    return transaction_controller.get_transactions_by_account(db, account_id)


@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return transaction_controller.get_transaction_by_id(db, transaction_id)


@router.post("/", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return transaction_controller.create_transaction(db, transaction)


@router.put("/{transaction_id}", response_model=TransactionResponse)
def update_transaction(transaction_id: int, transaction: TransactionUpdate, db: Session = Depends(get_db)):
    return transaction_controller.update_transaction(db, transaction_id, transaction)


@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return transaction_controller.delete_transaction(db, transaction_id)
