import os
from dotenv import load_dotenv

# O python-dotenv lê o arquivo .env e coloca as variáveis na memória do sistema
load_dotenv()

class Settings:
    """
    Centraliza as configurações lidas do arquivo .env.
    Isso permite que o código seja o mesmo em desenvolvimento e produção,
    mudando apenas os valores no arquivo de ambiente.
    """
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Sentinel API"
    PROJECT_VERSION: str = "1.0.0"  # Adicione esta linha aqui!
    
    # O os.getenv busca o valor no .env. Se não achar, usa o valor padrão (fallback)
    SECRET_KEY: str = os.getenv("SECRET_KEY", "chave-temporaria-de-dev")
    
    # O algoritmo HS256 (HMAC com SHA-256) garante a integridade do token JWT.
# Ele utiliza uma assinatura simétrica, onde apenas quem possui a SECRET_KEY
# pode validar a autenticidade dos dados transmitidos.
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./sentinel.db")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
settings = Settings()
