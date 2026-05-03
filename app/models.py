from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    role = Column(String(50), nullable=False)
    firebase_token = Column(String(255), unique=True, index=True)
    images = relationship("Image", back_populates="user")

class ClinicalInfo(Base):
    __tablename__ = "clinical_info"
    
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    use_pesticide = Column(String(10), nullable=False)
    family_skin_cancer_history = Column(String(10), nullable=False)
    family_cancer_history = Column(String(10), nullable=False)
    
    macro_body_region = Column(String(100))
    has_itched = Column(String(10), nullable=False)
    has_grown = Column(String(10), nullable=False)
    has_hurt = Column(String(10), nullable=False)
    has_changed = Column(String(10), nullable=False)
    has_bled = Column(String(10), nullable=False)
    has_elevation = Column(String(10), nullable=False)
    
    # Relacionamento inverso com a Imagem
    image = relationship("Image", back_populates="clinical_info", uselist=False)

class Image(Base):
    __tablename__ = "image"
    id = Column(Integer, primary_key=True, index=True)
    file_path = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("user.firebase_token"))
    clinical_info_id = Column(Integer, ForeignKey("clinical_info.id"))
    user = relationship("User", back_populates="images")
    clinical_info = relationship("ClinicalInfo", back_populates="image")