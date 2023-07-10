from pydantic import BaseModel
from typing import Optional

class RolCreateRequest(BaseModel):
  id : Optional[str]
  nombre : str
  abreviacion : str
  estado : bool