from fastapi import APIRouter
from ..schemas import OrgCreate
from ..services.org_service import OrgService

router = APIRouter(prefix="/org", tags=["Organization"])
service = OrgService()

@router.post("/create")
async def create_org(data: OrgCreate):
    return await service.create_org(data)
