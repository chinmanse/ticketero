from sqlalchemy import select, update as sqlalchemy_update
from sqlalchemy.orm import joinedload
from models.ticketModel import TicketModel
from models.categoriaModel import CategoriaModel
from utils.config import SessionLocal
from utils.response import dprint
# from utils.base import gender, beneficiary_type, document_type


class TicketService():
  def index():
    session = SessionLocal()
    users = session.query(TicketModel).all()
    return users
    

  def create():
    session = SessionLocal()
    categorias = session.query(CategoriaModel).filter(CategoriaModel.estado == True).all()
    return {
      'categorias':categorias
    }

  def store(request):
    try:
      session = SessionLocal()
      ticket = TicketModel()
      ticket.map(request)
      session.add(ticket)
      session.commit()
      return True,"OK"            
    except Exception as err:
      session.rollback()
      dprint(err.args[0])
      return False,err.args[0]
    finally:
      session.close()

  def getByUser(userId):
    session = SessionLocal() 
    tickets = session.query(TicketModel).\
      options(joinedload(TicketModel.user), joinedload(TicketModel.categoria)).\
      filter(TicketModel.user_id == userId).\
      all()
    return tickets


  def update(request, ticket_id):
    try:
      session = SessionLocal()
      ticket = session.query(TicketModel).filter_by(id=ticket_id).first() 
      ticket.update(request)
      session.commit()
      return True,"OK"            
    except Exception as err:
      session.rollback()
      dprint(err.args[0])
      return False,err.args[0]
    finally:
      session.close()
    # def edit(id):
    #     try:
    #         session = SessionLocal()
    #         relation = RelationshipService.index()
    #         branch_office = BranchOfficeService.index()
    #         result = session.scalars(select(BeneficiaryModel).where(BeneficiaryModel.id==id)).one()
    #         dprint(result)
    #         params = {
    #             'beneficiary_type':beneficiary_type, 
    #             'document_type':document_type,
    #             'extension': branch_office,
    #             'gender': gender,
    #             'relationship': relation,
    #         }
    #         return True, {
    #             'parameters':params,
    #             'data':result
    #         }          
    #     except Exception as err:
    #         session.rollback()
    #         dprint(err.args[0])
    #         return False,err.args[0]
    #     finally:
    #         session.close()


    


    # def delete(benficiary_id):
    #     try:
    #         session = SessionLocal()
    #         query = session.query(BeneficiaryModel).filter_by(id=benficiary_id).first() 
    #         session.delete(query)
    #         session.commit()
    #         return True,"OK"            
    #     except Exception as err:
    #         session.rollback()
    #         dprint(err.args[0])
    #         return False,err.args[0]
    #     finally:
    #         session.close()


    # def get_by_id(id):
    #     try:
    #         session = SessionLocal()
    #         result = session.scalars(select(BeneficiaryModel).where(BeneficiaryModel.id==id)).one()
    #         dprint(result)
    #         return True, result  
    #     except Exception as err:
    #         session.rollback()
    #         dprint(err.args[0])
    #         return False,err.args[0]
    #     finally:
    #         session.close()