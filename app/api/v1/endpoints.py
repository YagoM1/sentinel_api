from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.crud import user as user_crud
from app.schemas.user import UserCreate, UserOut
from app.db.session import get_db

router = APIRouter()

@router.post("/users/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Rota para cadastrar novos usuários.
    Verificar se o email já está em uso antes de criar.
    """
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Este email já está cadastrado no sistema."
        )
    return user_crud.create_user(db=db, user=user)

@router.get("/users/", response_model=List[UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Lista os usuários cadastrados.
    Utiliza os schema (UserOut) para esconder as senhas. 
    """
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users