from app.models.notification import Notification
from app.schemas.notification import NotificationCreate, NotificationBase
from app.repositories.base import BaseRepository

class NotificationRepository(BaseRepository[Notification, NotificationCreate, NotificationBase]):
    pass

notification_repo = NotificationRepository(Notification)
