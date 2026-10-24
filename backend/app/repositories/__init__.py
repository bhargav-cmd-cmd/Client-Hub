from app.repositories.user import user_repo
from app.repositories.client import client_repo
from app.repositories.project import project_repo
from app.repositories.document import document_repo
from app.repositories.notification import notification_repo
from app.repositories.activity import activity_repo

__all__ = [
    "user_repo",
    "client_repo",
    "project_repo",
    "document_repo",
    "notification_repo",
    "activity_repo",
]
