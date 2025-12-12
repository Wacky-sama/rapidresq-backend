from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import Base, engine
from app.routers import (
    auth,
    emergencies,
    messages, 
    users
)

# Load environment variables
load_dotenv()

# Initialize database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="RapidResQ Backend Prototype",
    description="Backend API for RapidResQ System",
    version="1.0.0"    
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
routers = [
    auth.router,
    users.router,
    emergencies.router,
    messages.router
]

for r in routers:
    app.include_router(r)

# Health check
@app.get("/", tags=["Health Check"])
def root():
    return {"message": "RapidResQ System Prototype backend is running!"}