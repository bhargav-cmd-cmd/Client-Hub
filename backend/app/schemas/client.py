from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict
from uuid import UUID

class ClientBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    company_name: Optional[str] = None
    address: Optional[str] = None
    status: Optional[str] = "Active"

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    company_name: Optional[str] = None
    address: Optional[str] = None
    status: Optional[str] = None

class ClientOut(ClientBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
