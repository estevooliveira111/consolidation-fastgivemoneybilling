from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Objeto de configuração do Alembic, fornece acesso aos valores do arquivo .ini
config = context.config

# Interpreta o arquivo de configuração para logging em Python.
# Esta linha basicamente configura os loggers.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importa o Base do SQLAlchemy e os modelos para autogerar migrations
from api.config.database import Base
from api.models.bank_model import Bank

# target_metadata é necessário para suporte ao 'autogenerate' do Alembic
target_metadata = Base.metadata

# Outras opções do config podem ser obtidas se necessário
# ex: minha_opcao_importante = config.get_main_option("minha_opcao_importante")


def run_migrations_offline() -> None:
    """Executa migrations em modo 'offline'.

    Configura o contexto apenas com a URL, sem precisar criar um Engine.
    O DBAPI não precisa estar disponível nesse modo.
    Chamadas a context.execute() aqui apenas geram o script de SQL.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa migrations em modo 'online'.

    Neste modo, precisamos criar um Engine e associar a conexão com o contexto.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


# Escolhe o modo de execução conforme o ambiente
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()