from sqlalchemy import select, update as sqlalchemy_update
from sqlalchemy.orm import joinedload
from models.userModel import UserModel
from models.rolModel import RolModel
from utils.config import SessionLocal
from utils.response import dprint
# from utils.base import gender, beneficiary_type, document_type


class UserService():
  def index():
    session = SessionLocal()
    users = session.query(UserModel).\
      options(joinedload(UserModel.rol)).\
      all()
    return users
    

  def create():
    session = SessionLocal()
    rols = session.query(RolModel).filter(RolModel.estado == True).all()
    return {
      'rols':rols
    }

  def store(request):
    try:
      session = SessionLocal()
      beneficiary = UserModel()
      beneficiary.map(request)
      session.add(beneficiary)
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


    # def update(request, benficiary_id):
    #     try:
    #         session = SessionLocal()
    #         query = session.query(BeneficiaryModel).filter_by(id=benficiary_id).first() 
    #         query.map(request)
    #         session.commit()
    #         return True,"OK"            
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