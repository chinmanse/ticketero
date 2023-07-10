from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from utils.config import Config
from typing import List
import uuid
from models.rolModel import RolModel
from models.ticketModel import TicketModel

class UserModel(Config):
  __tablename__ = "users"

  id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid1)
  rol_id = mapped_column(ForeignKey("rols.id"))
  nombre = Column(String(80))
  apellidos = Column(String(100))
  email = Column(String(150))
  estado = Column(Boolean)

  # Relations
  rol : Mapped["RolModel"] = relationship(back_populates="users")
  tickets: Mapped[List["TicketModel"]] = relationship(back_populates="user")
  respuestas: Mapped[List["RespuestaModel"]] = relationship(back_populates="user")
  

  def map(self, request):
    # self.id = request.id
    self.rol_id = request.rol_id
    self.nombre = request.nombre
    self.apellidos = request.apellidos
    self.email = request.email
    self.estado = request.estado
    
