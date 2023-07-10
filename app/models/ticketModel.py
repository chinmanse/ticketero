from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from utils.config import Config
from typing import List
import uuid

from models.categoriaModel import CategoriaModel

class TicketModel(Config):
  __tablename__ = "tickets"

  id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid1)
  user_id = mapped_column(ForeignKey("users.id")) 
  categoria_id = mapped_column(ForeignKey("categorias.id"))
  titulo = Column(String(150))
  descripcion = Column(String)
  estado = Column(Integer)

  # Relations
  user : Mapped["UserModel"] = relationship(back_populates="tickets")
  categoria : Mapped["CategoriaModel"] = relationship(back_populates="tickets")
  respuestas: Mapped[List["RespuestaModel"]] = relationship(back_populates="ticket")

  def map(self, request):
    self.user_id = request.user_id
    self.categoria_id = request.categoria_id
    self.titulo = request.titulo
    self.descripcion = request.descripcion
    self.estado = request.estado

  def update(self, request):
    self.estado = request["estado"]