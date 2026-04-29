from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

# Definimos uma classe base para compartilhar campos em comuns.
# Isso evita a repitição de código(DRY - Don't Repeat Yourself).
class UserBase(BaseModel):
    """
    Campos base que são compartilhados entre a criação e a leitura.
    O EmailStr valida automaticamente se a string segue o formato 'usuario@dominio.com'.
    """
    email: EmailStr

class UserCreate(UserBase):
    """
    Schema para a criação de usuário(Cadastro).
    Aqui exigimos a senha, que não será devolvida em nenhum GET por segurança.
    """
    password: str
    
class UserUpdate(UserBase):
    """
    Permite atualizar os dados do usuário.
    Todos os campos são opcionais para permitir atualizações parciais(PATCH).
    """
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_premium: Optional[bool] = None
    
class UserOut(UserBase):
    """
    Schemas de resposta (Output).
    Define o que o munde exterior pode ver sobre o usuário.
    A senha jamais deverar ser incluída aqui.
    """
    id: int
    is_active: bool
    is_premium: bool
    
    # Configuração para que o Pydantic consiga ler objetos do SQLAlchemy (ORM)
    model_config = ConfigDict(from_attributes=True)
    
# --- Schemas de Autenticação ---

class Token(BaseModel):
    """
    O contrato do token que será devolvido após um login bem-sucedido.
    """
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    """
    Estrutura dos dados que ficam "escondidos" dentro do token JTW.
    Geralmente usamos o email ou o ID do usuário.
    """
    email: Optional[str] = None