from pydantic import BaseModel, EmailStr

# ------------------------------
# Organization Schemas
# ------------------------------

class OrgCreate(BaseModel):
    organization_name: str
    email: EmailStr
    password: str


# ------------------------------
# Admin Schemas
# ------------------------------

class AdminCreate(BaseModel):
    email: EmailStr
    password: str
    organization_name: str


class AdminLogin(BaseModel):
    email: EmailStr
    password: str
