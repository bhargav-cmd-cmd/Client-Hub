from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field
from uuid import UUID

class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    email: EmailStr
    role: str = Field(..., description="Admin, Team Member, Client")
    client_id: Optional[UUID] = None
    is_active: Optional[bool] = True

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=255)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=128)
    role: str = Field("Client", description="Admin, Team Member, Client")
    client_id: Optional[UUID] = None

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[str] = None
    client_id: Optional[UUID] = None
    is_active: Optional[bool] = None

class UserOut(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    role: str
    client_id: Optional[UUID] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str
    role: str
    name: str

class TokenPayload(BaseModel):
    sub: Optional[str] = None
    role: Optional[str] = None
    name: Optional[str] = None
