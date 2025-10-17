import uuid
from faker import Faker

from sqlalchemy.orm import Session

from ..config.database import SessionLocal
from ..models.transaction_type_model import TransactionType

fake = Faker("pt_BR")


def create_transaction_types(db: Session):
    types = [
        {"name": "PIX_IN", "description": "Recebimento via Pix"},
        {"name": "PIX_OUT", "description": "Envio via Pix"},
        {"name": "BOLETO", "description": "Cobrança via boleto"},
        {"name": "BOLEPIX", "description": "BolePix (boleto convertido em pix)"},
        {"name": "CREDIT_CARD", "description": "Pagamento via cartão de crédito"},
        {"name": "DEBIT_CARD", "description": "Pagamento via cartão de débito"},
        {"name": "INTERNAL", "description": "Transferência interna entre carteiras"},
    ]

    created = []
    for t in types:
        existing = db.query(TransactionType).filter(TransactionType.name == t["name"]).first()
        if existing:
            created.append(existing)
            continue
        new = TransactionType(
            external_id=str(uuid.uuid4()),
            name=t["name"],
            description=t["description"],
            status="active",
        )
        db.add(new)
        created.append(new)

    db.commit()
    for c in created:
        db.refresh(c)
    return created

def run_seed(drop=False):
    db = SessionLocal()
    try:
        print("Criando TransactionTypes...")
        types = create_transaction_types(db)
        print(f"TransactionTypes criados/recuperados: {len(types)}")

        print("Seed finalizado com sucesso.")
    except Exception as e:
        db.rollback()
        print("Erro durante seed:", e)
    finally:
        db.close()


if __name__ == "__main__":
    run_seed()
