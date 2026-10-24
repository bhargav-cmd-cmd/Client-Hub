from app.models.activity import ActivityLog
from app.schemas.activity import ActivityLogCreate, ActivityLogBase
from app.repositories.base import BaseRepository

class ActivityLogRepository(BaseRepository[ActivityLog, ActivityLogCreate, ActivityLogBase]):
    pass

activity_repo = ActivityLogRepository(ActivityLog)
