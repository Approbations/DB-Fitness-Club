from repositories.admin_base import DataConnection
from datetime import date
from uuid import UUID

data_base = DataConnection()


class UserService:
    @staticmethod
    def get_all_clients():
        return data_base.get_all_clients()

    @staticmethod
    def get_user_by_id(client_id: UUID):
        return data_base.get_user_by_id(client_id)

    @staticmethod
    def delete_user(client_id: UUID):
        return data_base.delete_user(client_id)

    @staticmethod
    def get_user_memberships(client_id: UUID):
        return data_base.get_user_memberships(client_id)

    @staticmethod
    def get_client_visit(client_id: UUID):
        return data_base.get_client_visit(client_id)
