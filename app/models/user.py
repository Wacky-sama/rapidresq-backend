import enum
from sqlalchemy import Column, String, Boolean, Float, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database import Base
from datetime import datetime

class UserRole(str, enum.Enum):
    admin = "admin"
    user = "user"
    responder = "responder"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    last_name = Column(String(255), nullable=False)
    first_name = Column(String(255), nullable=False)
    middle_initial = Column(String(1), nullable=True)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    phone_number = Column(String(20))
    role = Column(Enum(UserRole), nullable=False)
    is_active = Column(Boolean, default=True)
    last_latitude = Column(Float)
    last_longitude = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
