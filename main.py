# app/main.py
from fastapi import FastAPI
from api.endpoints import auth, clients

# Создаем таблицы
# Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fitness Club API", version="1.0.0")

# Подключаем роутеры
# app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(clients.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Fitness Club API - Simple Email Authentication"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}