from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.config.database import Base, engine
from api.routes import bank_routes, bank_account_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Consolidation FastgiveMoney")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(bank_routes.router)
app.include_router(bank_account_routes.router)

@app.get("/")
def root():
    return {"message": "API FastGiveMoney Billing - OK 🚀"}
