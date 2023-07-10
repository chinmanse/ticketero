from fastapi import APIRouter
from controllers.ticketController import TicketController
from requests.ticketCreateRequest import TicketCreateRequest

router = APIRouter()

@router.get("/")
async def index():
    return TicketController.index()


@router.get("/create")
async def create():
    return TicketController.create()


@router.post("/store")
async def store(request: TicketCreateRequest):
    return TicketController.store(request)

@router.get("/getByUser")
async def getByUser(user_id):
    return TicketController.getByUser(user_id)



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