# consolidation-fastgivemoneybilling

Faz a consolidação dos pagamentos recebidos dentro do sistema.


# Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Rodar localmente
uvicorn api.main:app --reload



python -m api.seeds.seed


🧱 3. Gere a migração automática com Alembic
alembic revision --autogenerate -m "..."

🔁 4. Aplique a migração ao banco de dados
alembic upgrade head

alembic revision --autogenerate -m "add balance to bank_accounts"

alembic upgrade head