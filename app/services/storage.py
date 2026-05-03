import os
import uuid
from fastapi import UploadFile

UPLOAD_DIR = "/images"

def save_image_locally(file: UploadFile) -> str:
    # Gera um nome único para evitar sobrescrever arquivos
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
        
    return file_path