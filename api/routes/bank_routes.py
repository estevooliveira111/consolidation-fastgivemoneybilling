from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.config.database import get_db
from api.schemas.bank_schema import BankCreate, BankUpdate, BankResponse
from api.controllers import bank_controller

router = APIRouter(prefix="/banks", tags=["Bancos"])

@router.get("/", response_model=list[BankResponse])
def list_banks(db: Session = Depends(get_db)):
    """
    Retorna a lista de todos os bancos cadastrados.
    
    Args:
        db (Session): Sessão do banco de dados injetada pelo Depends.

    Returns:
        List[BankResponse]: Lista de objetos BankResponse.
    """
    return bank_controller.list_banks(db)

@router.get("/{external_id}", response_model=BankResponse)
def get_bank(external_id: str, db: Session = Depends(get_db)):
    """
    Retorna um banco específico baseado no external_id.
    
    Args:
        external_id (str): Identificador externo único do banco.
        db (Session): Sessão do banco de dados injetada pelo Depends.
    
    Raises:
        HTTPException: Se nenhum banco for encontrado com o external_id informado.
    
    Returns:
        BankResponse: Objeto BankResponse do banco encontrado.
    """
    bank = bank_controller.get_bank(db, external_id)
    if not bank:
        raise HTTPException(status_code=404, detail="Banco não encontrado")
    return bank

@router.post("/", response_model=BankResponse)
def create_bank(bank: BankCreate, db: Session = Depends(get_db)):
    """
    Cria um novo banco no banco de dados.
    
    Args:
        bank (BankCreate): Dados do banco a ser criado.
        db (Session): Sessão do banco de dados injetada pelo Depends.
    
    Returns:
        BankResponse: Objeto BankResponse do banco criado.
    """
    return bank_controller.create_bank(db, bank)