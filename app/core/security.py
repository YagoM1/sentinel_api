from passlib.context import CryptContext
from datetime import datetime,  timedelta
from typing import Any, Union
from jose import jwt
from app.core.config import settings

# Configuração do algoritmo de hash (Bcrypt)
# O rounds=12 define a "força" do hash,  tornando-o resistente a ataques de forças
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """
    Tranforma uma senha em texto puro em um hash seguro.
    Este hash é o que será salvo no bancos de dados.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hased_password: str) -> bool:
    """
    Verifica se a senha digitada no login bate com o hash salvo no banco
    """    
    return pwd_context.verify(plain_password, hased_password)

def create_access_token(subject: Union[str, Any], expire_delta: timedelta = None) -> str:
    """
    Gera um token JWT que o usuário usará para se autenticar nas próximas requisições.
    """
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    # O sub (subject) geralmente contém o email ou o ID do usuário.
    to_encode = {"exp": expire, "sub": str(subject)}

    # Assina o token usando a SECRET_KEY e o ALGORITHM que definimos no .env
    encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encode_jwt
        
