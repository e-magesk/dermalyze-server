from pydantic import BaseModel
from typing import Literal
from dataclasses import dataclass
from fastapi import Form

class UserCreate(BaseModel):
    full_name: str
    role: str
    firebase_token: str

class UserResponse(BaseModel):
    id: int
    full_name: str
    role: str
    firebase_token: str
    class Config:
        from_attributes = True

class ClinicalInfoCreate(BaseModel):
    age: int
    macro_body_region: str
    
    # Restrição rigorosa: a API só aceita esses 3 valores exatos
    family_cancer_history: Literal["true", "false", "unknown"]
    has_itched: Literal["true", "false", "unknown"]
    has_grown: Literal["true", "false", "unknown"]
    has_hurt: Literal["true", "false", "unknown"]
    has_changed: Literal["true", "false", "unknown"]
    has_bled: Literal["true", "false", "unknown"]
    has_elevation: Literal["true", "false", "unknown"]

class ClinicalInfoResponse(ClinicalInfoCreate):
    id: int

    class Config:
        from_attributes = True

@dataclass
class ClinicalForm:
    age: int = Form(...)
    macro_body_region: str = Form(...)
    family_cancer_history: Literal["true", "false", "unknown"] = Form(...)
    has_itched: Literal["true", "false", "unknown"] = Form(...)
    has_grown: Literal["true", "false", "unknown"] = Form(...)
    has_hurt: Literal["true", "false", "unknown"] = Form(...)
    has_changed: Literal["true", "false", "unknown"] = Form(...)
    has_bled: Literal["true", "false", "unknown"] = Form(...)
    has_elevation: Literal["true", "false", "unknown"] = Form(...)
    user_id: str = Form(...)
    prediction: str = Form(...)
    prediction_confidence: float = Form(...)
    prediction_type: str = Form(...)