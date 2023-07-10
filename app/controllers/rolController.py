from services.rolService import RolService
# from requests.credirProductCreateRequest import
from utils.response import success, error, dprint
from starlette.status import HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from requests.rolCreateRequest import RolCreateRequest

class RolController():
  def index():
    return success(RolService.index(), 'Success')
    
    
  def create():
    try:            
      return success(RolService.create(), 'Success')            
    except Exception as err:
      dprint(err)
      return error(
        message=err.args[0], code=HTTP_404_NOT_FOUND
      )


  def store(request: RolCreateRequest):        
    (resp, msg) = RolService.store(request)
    dprint(request)
    if(resp):
      return success(None, "Your insert was success")
    else:
      return error(msg, HTTP_404_NOT_FOUND)
        

    # def edit(id):
    #     (resp, msg) = BeneficiaryService.edit(id)
    #     if(resp):
    #         return success(msg, "Success")
    #     else:
    #         return error(msg, HTTP_204_NO_CONTENT)
        

    # def update(request: BeneficiaryRequest, id):   
    #     (resp, msg) = BeneficiaryService.update(request, id)
    #     dprint(request)
    #     if(resp):
    #         return success(None, "Your update was success")
    #     else:
    #         return error(msg, HTTP_404_NOT_FOUND)
        
    # def delete(id):   
    #     (resp, msg) = BeneficiaryService.delete(id)
    #     if(resp):
    #         return success(None, "Your delete was success")
    #     else:
    #         return error(msg, HTTP_404_NOT_FOUND)
        
        
    # def get_by_id(id):
    #     (resp, msg) = BeneficiaryService.get_by_id(id)
    #     if(resp):
    #         return success(msg, "Success")
    #     else:
    #         return error(msg, HTTP_204_NO_CONTENT)
        