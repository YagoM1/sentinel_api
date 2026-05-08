from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router
from app.api.v1 import login
from app.models.models import MonitorTarget
from app.api.v1 import monitors
from app.core.config import settings
from app.db.session import engine
from app.db.base_class import Base
from app.db import base
#importante para o SQLAlchemy encontrar os modelos

# Este comando cria as tabelas no banco de dados automaticamente se elas não existirem.
# Em projetos maiores, usamos o Alembic, mas para o início, isso agiliza o desenvolvimento.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="API de monitoramento assíncrono com autenticação JWT e criptografia."
)

# Incluíndo as rotas que criamos no arquivo de endpoints
# O prefixo /api/v1 ajuda a manter a organização e o versionamento.
app.include_router(api_router, prefix="/api/v1")

app.include_router(monitors.router,prefix="/api_v1/monitors", tags=["Monitors"])

app.include_router(login.router,prefix="/api/v1", tags=["login"])

@app.get("/")
def root():
    """
    Rota de boas-vindas para verificar se o servidor está online
    """
    return {"message": f"Bem-vindo à {settings.PROJECT_NAME}!"}