from typing import Optional, List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.models.client import Client
from app.schemas.user import UserCreate, UserUpdate
from app.repositories.user import user_repo
from app.repositories.client import client_repo
from app.core.security import get_password_hash

class UserService:
    def register_user(self, db: Session, *, user_in: UserCreate) -> User:
        """Register a new user, hash their password, and link/create Client organization if role is Client."""
        # 1. Check if user already exists
        existing_user = user_repo.get_by_email(db, email=user_in.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A user with this email address already exists.",
            )

        # 2. If role is Client, resolve or create their client profile
        resolved_client_id = user_in.client_id
        if user_in.role == "Client" and not resolved_client_id:
            # Create a default client organization for this client user
            new_client = Client(
                name=user_in.name,
                email=user_in.email,
                company_name=f"{user_in.name} Corp",
                status="Active",
            )
            db.add(new_client)
            db.commit()
            db.refresh(new_client)
            resolved_client_id = new_client.id
        elif user_in.role == "Client" and resolved_client_id:
            # Verify client exists
            client = client_repo.get(db, id=resolved_client_id)
            if not client:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Specified Client organization not found.",
                )

        # 3. Create user record
        hashed_password = get_password_hash(user_in.password)
        db_user = User(
            name=user_in.name,
            email=user_in.email,
            hashed_password=hashed_password,
            role=user_in.role,
            client_id=resolved_client_id,
            is_active=True,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_user_by_id(self, db: Session, user_id: str) -> Optional[User]:
        return user_repo.get(db, id=user_id)

    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        return user_repo.get_by_email(db, email=email)

    def list_users(self, db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        return user_repo.get_multi(db, skip=skip, limit=limit)

user_service = UserService()
