from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings


#A engine é o motor que traduz Python para SQL
engine = create_engine(settings.DATABASE_URL,connect_args={"check_same_thread": False}
)

#A SessionLocal é a fábrica de conexões. Cada requisição terá a sua.
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

#Base para os modelos herdarem
Base = declarative_base()

#Função de Dependencia: Garente que a conexão abre ao chegar em um pedido e feche ao terminar
def get_db():
    """
    Injeta a sessão do banco de dados
nas rotas da API.
    Isso garente que cada requisição tenha sua própria conexão,
     evitando vazamentos de memória e travamentos.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    