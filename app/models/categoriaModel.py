from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from utils.config import Config
from typing import List
import uuid

class CategoriaModel(Config):
  __tablename__ = "categorias"

  id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid1)
  nombre = Column(String(50))
  abreviacion = Column(String(3))
  estado = Column(Boolean)

  # Relations
  tickets: Mapped[List["TicketModel"]] = relationship(back_populates="categoria")

  def map(self, request):
    self.nombre = request.nombre
    self.abreviacion = request.abreviacion
    self.estado = request.estado