from datetime import datetime
from pydantic import BaseModel, ConfigDict
from uuid import UUID

class NotificationBase(BaseModel):
    user_id: UUID
    title: str
    message: str
    is_read: bool = False

class NotificationCreate(NotificationBase):
    pass

class NotificationOut(NotificationBase):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
