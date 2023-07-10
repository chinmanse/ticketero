from sqlalchemy import Column, String, ForeignKey, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from utils.config import Config
from typing import List
import uuid
from models.menuRolModel import MenuRolModel
class RolModel(Config):
  __tablename__ = "rols"

  id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid1)
  nombre = Column(String(50))
  abreviacion = Column(String(3))
  estado = Column(Boolean)

  # Relations
  users : Mapped[List["UserModel"]] = relationship(back_populates="rol")
  menu_rols : Mapped[List["MenuRolModel"]] = relationship(back_populates="rol")

  def map(self, request):
    self.nombre = request.nombre
    self.abreviacion = request.abreviacion
    self.estado = request.estado
    