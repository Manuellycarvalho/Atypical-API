from typing import Optional
from pydantic import BaseModel

class Personagem(BaseModel):
    id: Optional[int] = None
    nome: str | None = None
    idade: int | None = None