from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from app.models.emergency import EmergencyType, EmergencyStatus

# Used to create an emergency
class EmergencyCreate(BaseModel):
    user_id: UUID
    type: EmergencyType
    description: Optional[str] = None
    latitude: float
    longitude: float

# Used to return emergency info
class EmergencyOut(BaseModel):
    id: UUID
    user_id: UUID
    responder_id: Optional[UUID] = None
    type: EmergencyType
    description: Optional[str] = None
    status: EmergencyStatus
    latitude: float
    longitude: float

    class Config:
        from_attributes = True
