from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from .. import models, database, schemas
from ..services.storage import save_image_locally

router = APIRouter(prefix="/clinical", tags=["Clinical Information"])

@router.post("/upload")
async def upload_clinical_case(
    file: UploadFile = File(...),
    clinical_data: schemas.ClinicalForm = Depends(), # Modularizado aqui!
    db: Session = Depends(database.get_db)
):
    # 1. Salvar Informações Clínicas primeiro
    new_info = models.ClinicalInfo(
        age=clinical_data.age,
        gender=clinical_data.gender,
        fitzpatrick_skin_type=clinical_data.fitzpatrick_skin_type,
        macro_body_region=clinical_data.macro_body_region,
        use_pesticide=clinical_data.use_pesticide,
        family_skin_cancer_history=clinical_data.family_skin_cancer_history,
        family_cancer_history=clinical_data.family_cancer_history,
        has_itched=clinical_data.has_itched,
        has_grown=clinical_data.has_grown,
        has_hurt=clinical_data.has_hurt,
        has_changed=clinical_data.has_changed,
        has_bled=clinical_data.has_bled,
        has_elevation=clinical_data.has_elevation
    )
    db.add(new_info)
    db.flush() 

    path = save_image_locally(file)

    new_image = models.Image(
        file_path=path,
        user_id=clinical_data.user_id,
        clinical_info_id=new_info.id
    )
    db.add(new_image)
    
    db.commit()
    db.refresh(new_image)

    return {
        "message": "Caso clínico e imagem salvos com sucesso",
        "image_id": new_image.id,
        "path": path
    }