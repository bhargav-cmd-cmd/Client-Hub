import uuid
from sqlalchemy import Column, String, Text, ForeignKey, DateTime, Numeric, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

# Association Table for Many-to-Many relationship between Projects and Users (Team Members)
project_members = Table(
    "project_members",
    Base.metadata,
    Column("project_id", UUID(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"), primary_key=True),
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
)

class Project(Base):
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), default="Pending", nullable=False)  # Pending, In Progress, Review, Completed
    priority = Column(String(50), default="Medium", nullable=False)  # Low, Medium, High
    budget = Column(Numeric(12, 2), nullable=True)
    deadline = Column(DateTime(timezone=True), nullable=True)

    client_id = Column(UUID(as_uuid=True), ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    client = relationship("Client", back_populates="projects")
    team_members = relationship("User", secondary=project_members, back_populates="assigned_projects")
    documents = relationship("Document", back_populates="project", cascade="all, delete-orphan")
