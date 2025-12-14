from fastapi import FastAPI
from .db import init_indexes

from .routers.org_router import router as org_router
from .routers.admin_router import router as admin_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_indexes()

app.include_router(org_router, prefix="/org", tags=["Organization"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
