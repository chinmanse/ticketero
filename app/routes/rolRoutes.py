from fastapi import APIRouter
from controllers.rolController import RolController
from requests.rolCreateRequest import RolCreateRequest
router = APIRouter()

@router.get("/")
async def index():
    return RolController.index()


@router.get("/create")
async def create():
    return RolController.create()


@router.post("/store")
async def store(request: RolCreateRequest):
    return RolController.store(request)


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