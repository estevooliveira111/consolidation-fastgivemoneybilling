from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from api.config.database import get_db
from api.schemas.bank_account_schema import BankAccountCreate, BankAccountUpdate, BankAccountResponse
from api.controllers import bank_account_controller

router = APIRouter(prefix="/bank-accounts", tags=["Bank Accounts"])

@router.get("/", response_model=list[BankAccountResponse])
def list_accounts(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Número de registros a pular"),
    limit: int = Query(10, ge=1, le=100, description="Número máximo de registros a retornar")
):
    """Lista todas as contas bancárias com paginação"""
    return bank_account_controller.list_bank_accounts(db, skip=skip, limit=limit)

@router.get("/{external_id}", response_model=BankAccountResponse)
def get_account(external_id: str, db: Session = Depends(get_db)):
    """Busca uma conta bancária pelo external_id"""
    account = bank_account_controller.get_bank_account(db, external_id)
    if not account:
        raise HTTPException(status_code=404, detail="Conta bancária não encontrada")
    return account

@router.post("/", response_model=BankAccountResponse)
def create_account(account: BankAccountCreate, db: Session = Depends(get_db)):
    """Cria uma nova conta bancária"""
    return bank_account_controller.create_bank_account(db, account)

@router.put("/{external_id}", response_model=BankAccountResponse)
def update_account(external_id: str, account: BankAccountUpdate, db: Session = Depends(get_db)):
    """Atualiza uma conta bancária existente"""
    updated = bank_account_controller.update_bank_account(db, external_id, account)
    if not updated:
        raise HTTPException(status_code=404, detail="Conta bancária não encontrada")
    return updated

@router.delete("/{external_id}", response_model=BankAccountResponse)
def delete_account(external_id: str, db: Session = Depends(get_db)):
    """Deleta uma conta bancária pelo external_id"""
    deleted = bank_account_controller.delete_bank_account(db, external_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Conta bancária não encontrada")
    return deleted
