from database import DataConnection
from datetime import date

data_base = DataConnection()


class UserService:
    @staticmethod
    def get_all_clients():
        return data_base.get_all_data("client")

    @staticmethod
    def get_user_by_email(email: str):
        return data_base.get_user_by_email(email)

    @staticmethod
    def create_user(first_name: str, last_name: str, birth_date: date, email: str):
        return data_base.create_user(first_name, last_name, birth_date, email)

    @staticmethod
    def delete_user(email: str):
        return data_base.delete_user(email)
