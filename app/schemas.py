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
    
    class Config:
        from_attributes = True

class ClinicalInfoCreate(BaseModel):
    age: int
    gender: str
    macro_body_region: str
    
    # Restrição rigorosa: a API só aceita esses 3 valores exatos
    use_pesticide: Literal["sim", "nao", "nao_sei"]
    family_skin_cancer_history: Literal["sim", "nao", "nao_sei"]
    family_cancer_history: Literal["sim", "nao", "nao_sei"]
    has_itched: Literal["sim", "nao", "nao_sei"]
    has_grown: Literal["sim", "nao", "nao_sei"]
    has_hurt: Literal["sim", "nao", "nao_sei"]
    has_changed: Literal["sim", "nao", "nao_sei"]
    has_bled: Literal["sim", "nao", "nao_sei"]
    has_elevation: Literal["sim", "nao", "nao_sei"]

class ClinicalInfoResponse(ClinicalInfoCreate):
    id: int

    class Config:
        from_attributes = True

@dataclass
class ClinicalForm:
    age: int = Form(...)
    gender: str = Form(...)
    macro_body_region: str = Form(...)
    use_pesticide: Literal["sim", "nao", "nao_sei"] = Form(...)
    family_skin_cancer_history: Literal["sim", "nao", "nao_sei"] = Form(...)
    family_cancer_history: Literal["sim", "nao", "nao_sei"] = Form(...)
    has_itched: Literal["sim", "nao", "nao_sei"] = Form(...)
    has_grown: Literal["sim", "nao", "nao_sei"] = Form(...)
    has_hurt: Literal["sim", "nao", "nao_sei"] = Form(...)
    has_changed: Literal["sim", "nao", "nao_sei"] = Form(...)
    has_bled: Literal["sim", "nao", "nao_sei"] = Form(...)
    has_elevation: Literal["sim", "nao", "nao_sei"] = Form(...)
    user_id: int = Form(...)