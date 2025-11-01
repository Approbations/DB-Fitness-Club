import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from services.client_service import ClientService
from auth.dependencies import require_client_role, require_admin_role
from uuid import UUID


router = APIRouter()


@router.post("/clients")
async def create_client(first_name: str, last_name: str, birth_date: datetime.date, email: str,
                        current_user=Depends(require_client_role)):
    # Проверяем, нет ли уже клиента с таким email
    if ClientService.get_user_by_email(email):
        raise HTTPException(status_code=400, detail="Клиент с такой почтой уже существует.")
    ClientService.create_user(first_name, last_name, birth_date, email)
    return ClientService.get_user_by_email(email)


@router.get("/levels")
async def get_levels(current_client=Depends(require_client_role)):  # получение уровня всех абонементов
    return ClientService.get_levels()


@router.get("/my_membership")  # получение всех абонементов пользователя
async def get_my_membership(current_client=Depends(require_client_role)):
    client_id = UUID(current_client.user_id)
    return ClientService.get_my_membership(client_id)


@router.post("/new_membership")  # создание нового абонемента пользователем
async def new_membership(level: int, start_date: datetime.date, current_user=Depends(require_client_role)):
    client_id = UUID(current_user.user_id)
    ClientService.new_membership(client_id, level, start_date)
    return ClientService.get_my_membership(UUID(current_user.user_id))


@router.patch("/profile")  # обновление данных пользователя
async def update_profile(first_name: str, last_name: str, birth_date: datetime.date, email: str,
                         current_user=Depends(require_client_role)):
    client_id = UUID(current_user.user_id)
    ClientService.update_profile(client_id, first_name, last_name, birth_date, email)
    return ClientService.get_profile(client_id)


@router.get("/profile")
async def get_profile(current_user=Depends(require_client_role)):
    client_id = UUID(current_user.user_id)
    return ClientService.get_profile(client_id)
