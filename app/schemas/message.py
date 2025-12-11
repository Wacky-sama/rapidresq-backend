from pydantic import BaseModel
from uuid import UUID

# Used to send a message
class MessageCreate(BaseModel):
    emergency_id: UUID
    sender_id: UUID
    message: str

# Used to return message info
class MessageOut(BaseModel):
    id: UUID
    emergency_id: UUID
    sender_id: UUID
    message: str

    class Config:
        from_attributes = True
