import re
from sqlalchemy import Column, String, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from utils.config import Config
import uuid

class RespuestaModel(Config):
  __tablename__ = "respuestas"


  id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid1)
  user_id = mapped_column(ForeignKey("users.id")) 
  ticket_id = mapped_column(ForeignKey("tickets.id")) 
  observacion = Column(Text)
  estado_resultante = Column(Integer)

  # Relations
  user : Mapped["UserModel"] = relationship(back_populates="respuestas")
  ticket : Mapped["TicketModel"] = relationship(back_populates="respuestas")

  def map(self, request): 
    self.user_id = request.user_id
    self.ticket_id = request.ticket_id
    self.observacion = request.observacion
    self.estado_resultante = request.estado_resultante
    