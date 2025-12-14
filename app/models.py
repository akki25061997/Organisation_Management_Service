from pydantic import BaseModel
from typing import Optional

class Organization(BaseModel):
    id: Optional[str]
    organization_name: str

class Admin(BaseModel):
    id: Optional[str]
    email: str
    password: str
    org_id: Optional[str]
