from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from uuid import UUID

class ActivityLogBase(BaseModel):
    user_id: UUID
    action: str
    details: Optional[str] = None

class ActivityLogCreate(ActivityLogBase):
    pass

class ActivityLogOut(ActivityLogBase):
    id: UUID
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)
