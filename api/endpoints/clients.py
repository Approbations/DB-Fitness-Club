# app/api/endpoints/clients.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import date
from services.user_service import UserService

router = APIRouter()


@router.get("/clients/{email}")
def get_user_by_email(email: str):
    return UserService.get_user_by_email(email)


@router.get("/clients")
def get_all_clients():
    all_clients = UserService.get_all_clients()
    return {
        "total": len(all_clients),
        "clients": all_clients
    }


@router.post("/clients")
def create_client(first_name: str, last_name: str, birth_date: date, email: str):
    # Проверяем, нет ли уже клиента с таким email
    if UserService.get_user_by_email(email):
        raise HTTPException(status_code=400, detail="Клиент с такой почтой уже существует.")
    UserService.create_user(first_name, last_name, birth_date, email)
    return UserService.get_user_by_email(email)


@router.delete("/{email}")
def delete_user(email: str):
    UserService.delete_user(email)


# @router.get("/{email}/memberships")
# def get_user_memberships(email: str, db: Session = Depends(get_db)):
#     """Получение абонементов пользователя"""
#     user_service = UserService(db)
#     user = user_service.user_repo.get_by_email(email)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )
#
#     memberships = user_service.membership_repo.get_user_memberships(user.id)
#     return memberships


# @router.get("/{email}/bookings")
# def get_user_bookings(email: str, db: Session = Depends(get_db)):
#     """Получение бронирований пользователя"""
#     user_service = UserService(db)
#     bookings = user_service.booking_repo.get_user_bookings(email)
#     return bookings


# @router.post("/{email}/bookings/{class_id}")
# def create_booking(email: str, class_id: int, db: Session = Depends(get_db)):
#     """Создание бронирования для пользователя"""
#     user_service = UserService(db)
#
#     # Проверяем существование пользователя
#     user = user_service.user_repo.get_by_email(email)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )
#
#     # Создаем бронирование
#     booking = user_service.booking_repo.create(
#         user_email=email,
#         class_id=class_id,
#         status="confirmed"
#     )
#
#     return {"message": "Booking created successfully", "booking": booking}