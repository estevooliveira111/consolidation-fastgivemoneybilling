from fastapi import FastAPI

app = FastAPI(
    title="Consolidation API",
    description="API para autenticação e listagem de transações bancárias da plataforma Allebank.",
    version="1.0.0"
)
