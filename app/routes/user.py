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

@router.get("/{firebase_token}", response_model=schemas.UserResponse)
def get_user_by_token(firebase_token: str, db: Session = Depends(database.get_db)):
    print(f"Buscando usuário com token: {firebase_token}")
    user = db.query(models.User).filter(models.User.firebase_token == firebase_token).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado no banco central")  
    return user