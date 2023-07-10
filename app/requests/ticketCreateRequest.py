from pydantic import BaseModel
from typing import Optional

class TicketCreateRequest(BaseModel):
  id : Optional[str]
  user_id : str
  categoria_id : str
  titulo : str
  descripcion : str
  estado : int