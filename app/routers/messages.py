from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.message import Message
from app.schemas.message import MessageCreate, MessageOut

router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)

@router.post("/", response_model=MessageOut)
def send_message(msg: MessageCreate, db: Session = Depends(get_db)):
    new_msg = Message(
        emergency_id=msg.emergency_id,
        sender_id=msg.sender_id,
        message=msg.message
    )
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)
    return new_msg

@router.get("/emergency/{emergency_id}", response_model=list[MessageOut])
def get_messages(emergency_id: str, db: Session = Depends(get_db)):
    return db.query(Message).filter(Message.emergency_id == emergency_id).all()
