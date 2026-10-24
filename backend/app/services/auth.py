from typing import List, Optional
from datetime import timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.database import get_db
from app.core.security import verify_password, create_access_token, ALGORITHM
from app.models.user import User
from app.repositories.user import user_repo
from app.schemas.user import TokenPayload

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")

class AuthService:
    def authenticate(self, db: Session, email: str, password: str) -> Optional[User]:
        """Verify user credentials against email and password hash."""
        user = user_repo.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def get_current_user(self, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
        """Extract user from JWT token and verify they are active."""
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
            token_payload = TokenPayload(
                sub=email,
                role=payload.get("role"),
                name=payload.get("name")
            )
        except JWTError:
            raise credentials_exception

        user = user_repo.get_by_email(db, email=token_payload.sub)
        if not user:
            raise credentials_exception
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Inactive user profile"
            )
        return user

class RoleChecker:
    def __init__(self, allowed_roles: List[str]):
        """Dependency for enforcing Role-Based Access Control on endpoints."""
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: User = Depends(AuthService().get_current_user)) -> User:
        if current_user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource."
            )
        return current_user

auth_service = AuthService()
