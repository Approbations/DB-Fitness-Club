import datetime
from repositories.client_base import ClientConnection
from uuid import UUID

client_base = ClientConnection()


class ClientService:
    @staticmethod
    def create_user(first_name: str, last_name: str, birth_date: datetime.date, email: str):
        return client_base.create_user(first_name, last_name, birth_date, email)

    @staticmethod
    def get_levels():
        return client_base.get_levels()

    @staticmethod
    def get_my_membership(client_id: UUID):
        return client_base.get_my_membership(client_id)

    @staticmethod
    def new_membership(client_id: UUID, level: int, start_date: datetime.date):
        client_base.new_membership(client_id, level, start_date)

    @staticmethod
    def update_profile(client_id: UUID, first_name: str, last_name: str, birth_date: datetime.date, email: str):
        client_base.update_profile(client_id, first_name, last_name, birth_date, email)

    @staticmethod
    def get_profile(client_id: UUID):
        client_base.get_profile(client_id)