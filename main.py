import jwt
from fastapi import FastAPI
from api.endpoints import client, admin
from datetime import timedelta, datetime


app = FastAPI(title="Fitness Club API", version="1.0.0")

# Подключаем роутеры
app.include_router(client.router, prefix="/client", tags=["client"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])


@app.get("/")
def read_root():
    return {"message": "Fitness Club API - Simple Email Authentication"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/generate-token")  # токен только для тестирования
def generate_token(role: str = "client", user_id: str = "a149a6df-7f91-4fe9-88bb-7c7decf51be3"):
    payload = {
        "sub": user_id,
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, "your-secret-key-here", algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}
