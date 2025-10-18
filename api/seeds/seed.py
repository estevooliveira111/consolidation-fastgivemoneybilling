import uuid
from faker import Faker
from sqlalchemy.orm import Session

from ..config.database import SessionLocal
from ..models.transaction_type_model import TransactionType
from ..models.bank_model import Bank

fake = Faker("pt_BR")


def create_transaction_types(db: Session):
    types = [
        {"name": "PIX_IN", "description": "Recebimento via Pix"},
        {"name": "PIX_OUT", "description": "Envio via Pix"},
        {"name": "BOLETO", "description": "Cobrança via boleto"},
        {"name": "BOLEPIX", "description": "BolePix (boleto convertido em Pix)"},
        {"name": "CREDIT_CARD", "description": "Pagamento via cartão de crédito"},
        {"name": "DEBIT_CARD", "description": "Pagamento via cartão de débito"},
        {"name": "INTERNAL", "description": "Transferência interna entre carteiras"},

        {"name": "TAXA_PIX_IN", "description": "Taxa pelo recebimento via Pix"},
        {"name": "TAXA_PIX_OUT", "description": "Taxa pelo envio via Pix"},
        {"name": "TAXA_BOLETO", "description": "Taxa pela cobrança via boleto"},
        {"name": "TAXA_BOLEPIX", "description": "Taxa pelo BolePix (boleto convertido em Pix)"},
        {"name": "TAXA_CREDIT_CARD", "description": "Taxa pelo pagamento via cartão de crédito"},
        {"name": "TAXA_DEBIT_CARD", "description": "Taxa pelo pagamento via cartão de débito"},
        {"name": "TAXA_INTERNAL", "description": "Taxa pela transferência interna entre carteiras"},
    ]

    created = []
    for t in types:
        existing = db.query(TransactionType).filter(TransactionType.name == t["name"]).first()
        if existing:
            existing.description = t["description"]
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


def create_banks(db: Session):
    banks = [
        {"name": "BB", "full_name": "Banco do Brasil S.A.", "code": "001", "ispb": "00000000"},
        {"name": "Sicredi", "full_name": "Sicredi Cooperativa de Crédito", "code": "748", "ispb": "00000001"},
        {"name": "Sicoob", "full_name": "Sicoob Cooperativa de Crédito", "code": "756", "ispb": "00000002"},
    ]

    created = []
    for b in banks:
        existing = db.query(Bank).filter(Bank.code == b["code"]).first()
        if existing:
            existing.name = b["name"]
            existing.full_name = b["full_name"]
            existing.ispb = b["ispb"]
            created.append(existing)
            continue

        new_bank = Bank(
            external_id=str(uuid.uuid4()),
            name=b["name"],
            full_name=b["full_name"],
            code=b["code"],
            ispb=b["ispb"],
            country="BR"
        )
        db.add(new_bank)
        created.append(new_bank)

    db.commit()
    for c in created:
        db.refresh(c)
    return created


def run_seed(drop=False):
    db = SessionLocal()
    try:
        print("Criando TransactionTypes e tipos de Taxas...")
        types = create_transaction_types(db)
        print(f"TransactionTypes criados/atualizados: {len(types)}")

        print("Criando bancos...")
        banks = create_banks(db)
        print(f"Bancos criados/atualizados: {len(banks)}")

        print("Seed finalizado com sucesso.")
    except Exception as e:
        db.rollback()
        print("Erro durante seed:", e)
    finally:
        db.close()


if __name__ == "__main__":
    run_seed()
