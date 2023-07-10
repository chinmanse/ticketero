from pydantic import BaseModel
from typing import Optional

class CategoriaCreateRequest(BaseModel):
  id : Optional[str]
  nombre : str
  abreviacion : str
  estado : bool