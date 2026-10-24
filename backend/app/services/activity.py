from sqlalchemy.orm import Session
from app.models.activity import ActivityLog
from app.schemas.activity import ActivityLogCreate
from app.repositories.activity import activity_repo

class ActivityLogService:
    def log_activity(self, db: Session, *, user_id: str, action: str, details: str = None) -> ActivityLog:
        """Create a new activity log entry in the database."""
        db_log = ActivityLog(
            user_id=user_id,
            action=action,
            details=details
        )
        db.add(db_log)
        db.commit()
        db.refresh(db_log)
        return db_log

activity_service = ActivityLogService()
