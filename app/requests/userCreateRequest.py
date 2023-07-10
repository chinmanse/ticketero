from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreateRequest(BaseModel):
  id : Optional[str]
  rol_id : str
  nombre : str
  apellidos : str
  email : EmailStr
  estado : Optional[bool]