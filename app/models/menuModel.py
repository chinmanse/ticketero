from sqlalchemy import Column, String, ForeignKey, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from utils.config import Config
from typing import List
import uuid

class MenuModel(Config):
  __tablename__ = "menus"

  id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid1)
  nombre = Column(String(50))
  abreviacion = Column(String(3))
  url = Column(String(150))
  estado = Column(Boolean)

  # Relations
  menu_rols: Mapped[List["MenuRolModel"]] = relationship(back_populates="menu")

  def map(self, request):
    self.id = request.id
    self.nombre = request.nombre
    self.abreviacion = request.abreviacion
    self.url = request.url
    self.estado = request.estado