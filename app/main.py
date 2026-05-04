import os
from fastapi import FastAPI
from .database import engine, Base
from .routes import user, clinical
from fastapi.middleware.cors import CORSMiddleware

# Cria as tabelas ao iniciar (Ideal para o ambiente LIFE/UFES)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Dermalyze API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Em produção, use apenas o domínio do app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Verifica diretório de imagens
@app.on_event("startup")
def startup():
    os.makedirs("/images", exist_ok=True)

# Registra as rotas
app.include_router(user.router)
app.include_router(clinical.router)

@app.get("/")
def root():
    return {"message": "Dermalyze Backend is running"}