from fastapi import APIRouter
from ..services.auth_service import AuthService
from ..schemas import AdminCreate, AdminLogin

router = APIRouter()
service = AuthService()

@router.post("/create")
async def create_admin(data: AdminCreate):
    return await service.create_admin(data)

@router.post("/login")
async def login(data: AdminLogin):
    return await service.login(data)
