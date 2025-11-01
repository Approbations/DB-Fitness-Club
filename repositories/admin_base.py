import psycopg2
import logging
from typing import Tuple
from uuid import UUID
from psycopg2.extras import RealDictCursor

logger = logging.getLogger(__name__)


class DataBase:
    def __init__(self):
        self.dbname = "fitness"
        self.user = "postgres"
        self.password = "qwerty"
        self.host = "localhost"
        self.port = "5432"

    def _get_connection(self):
        conn_config = {
            'dbname': self.dbname,
            'user': self.user,
            'password': self.password,
            'host': self.host,
            'port': self.port
        }
        return psycopg2.connect(**conn_config)

    def _execute_query(self, query: str, params: Tuple = None, fetch: bool = False):
        try:
            with self._get_connection() as conn:
                conn.autocommit = True
                with conn.cursor() as cur:
                    cur.execute(query, params)
                    if fetch:
                        return cur.fetchall()
                    return cur
        except psycopg2.Error as e:
            logger.error(f"Ошибка в базе данных: {e}")
            raise

    # получение всех данных из какой-либо таблицы
    def get_all_data(self, table: str):
        query = f"""SELECT * FROM {table};"""

        try:
            with self._get_connection() as conn:
                conn.autocommit = True
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute(query)
                    ans = cur.fetchall()
                    return ans
        except psycopg2.Error as e:
            logger.error(f"Ошибка в получении данных: {e}")
            return []


class DataConnection(DataBase):
    def get_all_clients(self):
        return DataBase.get_all_data(self, table="client")

    def get_user_by_id(self, client_id: UUID):
        query = f"""SELECT * FROM client WHERE id = '{client_id}';"""

        try:
            with self._get_connection() as conn:
                conn.autocommit = True
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute(query)
                    ans = cur.fetchall()
                    return ans
        except psycopg2.Error as e:
            logger.error(f"Ошибка в получении данных: {e}")
            return []

    def delete_user(self, client_id: UUID):
        delete_query = f"DELETE FROM client WHERE id = '{client_id}';"

        try:
            with self._get_connection() as conn:
                conn.autocommit = True
                with conn.cursor() as cur:
                    cur.execute(delete_query)

        except Exception as e:
            logger.error(f"Ошибка при удалении документов: {e}")
            raise

    def get_user_memberships(self, client_id: UUID):
        query = f"""SELECT gym_membership.id, start_date, level, status FROM gym_membership
                WHERE id_client = '{client_id}';"""

        try:
            with self._get_connection() as conn:
                conn.autocommit = True
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute(query)
                    ans = cur.fetchall()
                    return ans
        except psycopg2.Error as e:
            logger.error(f"Ошибка в получении абонементов: {e}")
            return []

    def get_client_visit(self, client_id: UUID):
        query = f"""SELECT * FROM client_visit WHERE id_client = '{client_id}';"""

        try:
            with self._get_connection() as conn:
                conn.autocommit = True
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute(query)
                    ans = cur.fetchall()
                    return ans
        except psycopg2.Error as e:
            logger.error(f"Ошибка в получении данных: {e}")
            return []
