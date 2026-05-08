from datetime import timedelta
from fastapi import APIRouter, Depends,HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core import security
from app.models.models import User
from app.schemas.token import Token
from app.core.config import settings


router = APIRouter()

@router.post("/login/access-token", response_model=Token)
def login_access_token(
    db: Session = Depends(get_db),
    from_data: OAuth2PasswordRequestForm = Depends()
):
    """
    OAuth2 compatível com o login, obtém um access token para futuras rrquisições.
    o 'username' do from_data será o e-mail do usuário.
    """
    
    # 1. Buscar o usuário pelo e-mail
    user = db.query(User).filter(User.email == from_data.username).first()
    
    # 2. Verifica se existe e se a senha está correta
    if not user or not security.verify_password(from_data.password,user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail ou senha incorretos"
        )
    elif not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Usuário inativo'
        )
        
    # 3. Gera o tempo de expiração e o Token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(user.id, expire_delta=access_token_expires
        ),
        "token_type": "bearer"
    }
    