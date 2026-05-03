from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/user", tags=["Authentication"])

@router.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Verifica se o token já existe
    db_user = db.query(models.User).filter(models.User.firebase_token == user.firebase_token).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Token já registrado")
    
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user