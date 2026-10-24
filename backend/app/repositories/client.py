from typing import Optional
from sqlalchemy.orm import Session
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientUpdate
from app.repositories.base import BaseRepository

class ClientRepository(BaseRepository[Client, ClientCreate, ClientUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[Client]:
        """Fetch a single client organization by email address."""
        return db.query(self.model).filter(self.model.email == email).first()

client_repo = ClientRepository(Client)
