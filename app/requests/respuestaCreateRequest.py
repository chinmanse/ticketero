from pydantic import BaseModel
from typing import Optional

class RespuestaCreateRequest(BaseModel):
  id : Optional[str]
  user_id : str
  ticket_id : str
  observacion : str
  estado_resultante : int
