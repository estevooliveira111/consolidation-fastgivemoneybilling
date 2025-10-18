from sqlalchemy.orm import Session, joinedload
from api.repositories import wallet_repository
from api.schemas.wallet_schema import WalletCreate, WalletUpdate

def list_wallets(db: Session, skip: int = 0, limit: int = 10):
    """
    Lista todas as wallets com a relação bank_account carregada,
    aplicando paginação.
    """
    return (
        db.query(wallet_repository.Wallet)
        .options(joinedload(wallet_repository.Wallet.bank_account))
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_wallet(db: Session, wallet_id: int):
    return (
        db.query(wallet_repository.Wallet)
        .options(joinedload(wallet_repository.Wallet.bank_account))
        .filter(wallet_repository.Wallet.id == wallet_id)
        .first()
    )

def create_wallet(db: Session, wallet: WalletCreate):
    return wallet_repository.create_wallet(db, wallet)

def update_wallet(db: Session, wallet_id: int, wallet: WalletUpdate):
    return wallet_repository.update_wallet(db, wallet_id, wallet)

def delete_wallet(db: Session, wallet_id: int):
    return wallet_repository.delete_wallet(db, wallet_id)