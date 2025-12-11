import enum
from sqlalchemy import Column, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database import Base
from datetime import datetime

class EmergencyType(str, enum.Enum):
    vehicle_accident = "vehicle_accident"
    medical = "medical"
    fire = "fire"
    crime = "crime"
    disaster = "disaster"
    other = "other"

class EmergencyStatus(str, enum.Enum):
    pending = "pending"
    accepted = "accepted"
    enroute = "enroute"
    resolved = "resolved"
    canceled = "canceled"

class Emergency(Base):
    __tablename__ = "emergencies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    responder_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    type = Column(Enum(EmergencyType), nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(EmergencyStatus), nullable=False, default=EmergencyStatus.pending)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
