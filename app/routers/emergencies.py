from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.emergency import Emergency, EmergencyStatus
from app.schemas.emergency import EmergencyCreate, EmergencyOut

router = APIRouter(
    prefix="/emergencies",
    tags=["Emergencies"]
)

@router.post("/", response_model=EmergencyOut, tags=["Emergencies"])
def create_emergency(emergency: EmergencyCreate, db: Session = Depends(get_db)):
    new_emergency = Emergency(
        user_id=emergency.user_id,
        type=emergency.type,
        description=emergency.description,
        latitude=emergency.latitude,
        longitude=emergency.longitude
    )
    db.add(new_emergency)
    db.commit()
    db.refresh(new_emergency)
    return new_emergency

@router.get("/", response_model=list[EmergencyOut], tags=["Emergencies"])
def list_emergencies(db: Session = Depends(get_db)):
    return db.query(Emergency).all()

@router.put("/{emergency_id}/assign", response_model=EmergencyOut, tags=["Emergencies"])
def assign_responder(emergency_id: str, responder_id: str, db: Session = Depends(get_db)):
    emergency = db.query(Emergency).filter(Emergency.id == emergency_id).first()
    if not emergency:
        raise HTTPException(status_code=404, detail="Emergency not found")
    emergency.responder_id = responder_id
    emergency.status = EmergencyStatus.accepted
    db.commit()
    db.refresh(emergency)
    return emergency
