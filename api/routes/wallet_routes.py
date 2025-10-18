from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from api.config.database import get_db
from api.schemas.wallet_schema import WalletCreate, WalletUpdate, WalletResponse
from api.controllers import wallet_controller

router = APIRouter(prefix="/wallets", tags=["Carteiras"])


@router.get("/", response_model=list[WalletResponse])
def list_wallets(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="Número de registros a pular"),
    limit: int = Query(10, ge=1, le=100, description="Número máximo de registros a retornar")
):
    """
    Lista todas as wallets com a relação bank_account carregada,
    aplicando paginação.
    """
    return wallet_controller.list_wallets(db, skip=skip, limit=limit)

@router.get("/{wallet_id}", response_model=WalletResponse)
def get_wallet(wallet_id: int, db: Session = Depends(get_db)):
    wallet = wallet_controller.get_wallet(db, wallet_id)
    if not wallet:
        raise HTTPException(status_code=404, detail="Carteira não encontrada")
    return wallet

@router.post("/", response_model=WalletResponse)
def create_wallet(wallet: WalletCreate, db: Session = Depends(get_db)):
    return wallet_controller.create_wallet(db, wallet)

@router.put("/{wallet_id}", response_model=WalletResponse)
def update_wallet(wallet_id: int, wallet: WalletUpdate, db: Session = Depends(get_db)):
    updated = wallet_controller.update_wallet(db, wallet_id, wallet)
    if not updated:
        raise HTTPException(status_code=404, detail="Carteira não encontrada")
    return updated

@router.delete("/{wallet_id}")
def delete_wallet(wallet_id: int, db: Session = Depends(get_db)):
    deleted = wallet_controller.delete_wallet(db, wallet_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Carteira não encontrada")
    return {"message": "Carteira excluída com sucesso"}
