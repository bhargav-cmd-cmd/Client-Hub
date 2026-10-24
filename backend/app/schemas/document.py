from datetime import datetime
from pydantic import BaseModel, ConfigDict
from uuid import UUID

class DocumentBase(BaseModel):
    name: str
    file_url: str
    file_type: str
    project_id: UUID

class DocumentCreate(DocumentBase):
    uploaded_by: UUID

class DocumentOut(DocumentBase):
    id: UUID
    uploaded_by: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
