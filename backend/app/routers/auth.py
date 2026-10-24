from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserCreate, UserOut, Token
from app.services.user import user_service
from app.services.auth import auth_service
from app.services.activity import activity_service
from app.core.security import create_access_token
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    """Register a new user account."""
    new_user = user_service.register_user(db, user_in=user_in)
    # Log registration action
    activity_service.log_activity(
        db,
        user_id=new_user.id,
        action="Register",
        details=f"User registered with role: {new_user.role}"
    )
    return new_user

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Standard OAuth2 login flow. Returns JWT access token."""
    user = auth_service.authenticate(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )
    elif not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user profile",
        )

    access_token = create_access_token(subject=user.email, role=user.role, name=user.name)

    # Log login action
    activity_service.log_activity(
        db,
        user_id=user.id,
        action="Login",
        details="User logged in successfully"
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role,
        "name": user.name
    }

@router.get("/me", response_model=UserOut)
def read_current_user(current_user: User = Depends(auth_service.get_current_user)):
    """Fetch profile data for currently authenticated session."""
    return current_user
