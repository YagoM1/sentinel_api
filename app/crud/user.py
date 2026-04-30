from sqlalchemy.orm import Session
from app.models.models import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

def get_user_by_email(db: Session, email: str):
    """
    Busca um usuário no banco pelo email.
    Útil para verificar se um usuário já existe antes do cadastro.
    """
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session,  user: UserCreate):
    """
    Transforma o Schemas (Pydantic) em um Model (SQLAlchemy).
    Aplica o hash na senha antes de salvar por segurança.
    """
    # 1. Geramos um hash da senha enviada
    hashed_password = get_password_hash(user.password)

    # 2. Criamos um objeto no SQLAlchemy
    db_user = User(
        email=user.email,
        hashed_password=hashed_password
    )

    # 3. Salvamos no banco de dados.
    db.add(db_user)
    db.commit()
    db.refresh(db_user) # Atualiza o objeto com o ID gerado pelo banco

    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Retorna uma lista de usuários com paginação (skip/limit).
    Essencial para performace para quando o banco crecer.
    """
    return db.query(User).offset(skip).limit(limit).all()