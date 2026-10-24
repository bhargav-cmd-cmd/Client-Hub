from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserCreate, UserOut
from app.services.user import user_service
from app.services.auth import RoleChecker
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

# Admin-only dependency
admin_required = RoleChecker(allowed_roles=["Admin"])

@router.get("/", response_model=List[UserOut])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    """Retrieve all users in the system. Admin role required."""
    return user_service.list_users(db, skip=skip, limit=limit)

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    """Create a new user profile. Admin role required."""
    return user_service.register_user(db, user_in=user_in)
