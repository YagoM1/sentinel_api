from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenPayload(BaseModel):
    # O sub aqui vai guarda o ID do usuário que vem dentro do JWT
    sub: Optional[int] = None