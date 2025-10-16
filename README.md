# consolidation-fastgivemoneybilling

Faz a consolidação dos pagamentos recebidos dentro do sistema.


# Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Rodar localmente
uvicorn api.main:app --reload