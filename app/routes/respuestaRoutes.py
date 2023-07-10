from fastapi import APIRouter
from controllers.respuestaController import RespuestaController
from requests.respuestaCreateRequest import RespuestaCreateRequest
router = APIRouter()

@router.get("/")
async def index():
    return RespuestaController.index()


@router.get("/create")
async def create():
    return RespuestaController.create()


@router.post("/store")
async def store(request: RespuestaCreateRequest):
    return RespuestaController.store(request)

@router.get("/get_by_ticket")
async def get_by_ticket(ticketId):
    return RespuestaController.get_by_ticket(ticketId)

# @router.get("/edit/{id}")
# async def edit(id):
#     return BeneficiaryController.edit(id)


# @router.patch("/update/{id}")
# async def update(request: BeneficiaryRequest, id):
#     return BeneficiaryController.update(request, id)


# @router.delete("/delete/{id}")
# async def delete(id):
#     return BeneficiaryController.delete(id)


# @router.get("/get_by_id/{id}")
# async def get_by_id(id):
#     return BeneficiaryController.get_by_id(id)