from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.config.database import get_db
from api.schemas.transaction_type_schema import TransactionTypeResponse
from api.controllers import transaction_type_controller

router = APIRouter(prefix="/transaction-types", tags=["Tipo de Transações"])


@router.get("/", response_model=list[TransactionTypeResponse])
def list_transaction_types(db: Session = Depends(get_db)):
    return transaction_type_controller.list_transaction_types(db)


@router.get("/{type_id}", response_model=TransactionTypeResponse)
def get_transaction_type(type_id: int, db: Session = Depends(get_db)):
    type_obj = transaction_type_controller.get_transaction_type(db, type_id)
    if not type_obj:
        raise HTTPException(status_code=404, detail="Tipo de transação não encontrado")
    return type_obj
