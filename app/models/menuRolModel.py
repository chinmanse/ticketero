from email.policy import default
from sqlalchemy import Column, String, ForeignKey, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from utils.config import Config
from typing import List
import uuid
from models.menuModel import MenuModel

class MenuRolModel(Config):
  __tablename__ = "menu_rols"

  id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid1)
  rol_id = mapped_column(ForeignKey("rols.id"))
  menu_id = mapped_column(ForeignKey("menus.id"))
  can_udpate = Column(Boolean, default= True)
  can_delete = Column(Boolean, default= True)
  can_view = Column(Boolean, default= True)
  estado = Column(Boolean, default= True)

  # Relations
  rol : Mapped["RolModel"] = relationship(back_populates="menu_rols")
  menu : Mapped["MenuModel"] = relationship(back_populates="menu_rols")

  def map(self, request):
    self.rol_id = request.rol_id
    self.menu_id = request.menu_id
    self.can_udpate = request.can_udpate
    self.can_delete = request.can_delete
    self.can_view = request.can_view
    self.estado = request.estado
