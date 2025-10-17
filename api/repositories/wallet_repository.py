from sqlalchemy.orm import Session
from api.models.wallet_model import Wallet
from api.schemas.wallet_schema import WalletCreate, WalletUpdate

def get_all_wallets(db: Session):
    return db.query(Wallet).all()

def get_wallet_by_id(db: Session, wallet_id: int):
    return db.query(Wallet).filter(Wallet.id == wallet_id).first()

def create_wallet(db: Session, wallet: WalletCreate):
    db_wallet = Wallet(**wallet.dict())
    db.add(db_wallet)
    db.commit()
    db.refresh(db_wallet)
    return db_wallet

def update_wallet(db: Session, wallet_id: int, wallet_data: WalletUpdate):
    wallet = get_wallet_by_id(db, wallet_id)
    if not wallet:
        return None

    for key, value in wallet_data.dict(exclude_unset=True).items():
        setattr(wallet, key, value)

    db.commit()
    db.refresh(wallet)
    return wallet

def delete_wallet(db: Session, wallet_id: int):
    wallet = get_wallet_by_id(db, wallet_id)
    if not wallet:
        return None
    db.delete(wallet)
    db.commit()
    return wallet
