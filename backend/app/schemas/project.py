from datetime import datetime
from typing import Optional, List
from decimal import Decimal
from pydantic import BaseModel, ConfigDict
from uuid import UUID
from app.schemas.user import UserOut

class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    status: Optional[str] = "Pending"  # Pending, In Progress, Review, Completed
    priority: Optional[str] = "Medium"  # Low, Medium, High
    budget: Optional[Decimal] = None
    deadline: Optional[datetime] = None
    client_id: UUID

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    budget: Optional[Decimal] = None
    deadline: Optional[datetime] = None
    client_id: Optional[UUID] = None
    team_member_ids: Optional[List[UUID]] = None

class ProjectOut(ProjectBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    team_members: List[UserOut] = []

    model_config = ConfigDict(from_attributes=True)
