from fastapi import APIRouter, Depends, HTTPException, status
from services.admin_service import UserService
from auth.dependencies import require_client_role, require_admin_role
from uuid import UUID

router = APIRouter()


@router.get("/clients/{client_id}")
async def get_user_by_id(client_id: UUID, current_user=Depends(require_admin_role)):
    return UserService.get_user_by_id(client_id)


@router.get("/clients")
async def get_all_clients(current_user=Depends(require_admin_role)):
    all_clients = UserService.get_all_clients()
    return {
        "total": len(all_clients),
        "clients": all_clients
    }


@router.delete("/{client_id}")
async def delete_user(client_id: UUID, current_user=Depends(require_admin_role)):
    UserService.delete_user(client_id)


@router.get("/{client_id}/memberships")
async def get_user_memberships(client_id: UUID,
                               current_user=Depends(require_admin_role)):  # Получение абонементов пользователя
    return UserService.get_user_memberships(client_id)


@router.get("/{client_id}/visit")
async def get_client_visit(client_id: UUID, current_user=Depends(require_admin_role)):  # получение всех посещений клиента
    return UserService.get_client_visit(client_id)
