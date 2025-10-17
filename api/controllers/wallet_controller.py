from sqlalchemy.orm import Session
from api.repositories import wallet_repository
from api.schemas.wallet_schema import WalletCreate, WalletUpdate

def list_wallets(db: Session):
    return wallet_repository.get_all_wallets(db)

def get_wallet(db: Session, wallet_id: int):
    return wallet_repository.get_wallet_by_id(db, wallet_id)

def create_wallet(db: Session, wallet: WalletCreate):
    return wallet_repository.create_wallet(db, wallet)

def update_wallet(db: Session, wallet_id: int, wallet: WalletUpdate):
    return wallet_repository.update_wallet(db, wallet_id, wallet)

def delete_wallet(db: Session, wallet_id: int):
    return wallet_repository.delete_wallet(db, wallet_id)
