import psycopg2
import logging
from datetime import date
from typing import Tuple
from psycopg2.extras import RealDictCursor

logger = logging.getLogger(__name__)


class DataConnection:
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

    def get_user_by_email(self, email: str):
        query = f"""SELECT * FROM client WHERE email = '{email}';"""

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

    def create_user(self, first_name: str, last_name: str, birth_date: date, email: str):
        insert_query = f"""INSERT INTO client (first_name, last_name, birth_date, email) VALUES ('{first_name}', '{last_name}', '{birth_date}', '{email}');"""

        try:
            with self._get_connection() as conn:
                conn.autocommit = True
                with conn.cursor() as cur:
                    cur.execute(insert_query)
        except Exception as e:
            logger.error(f"Ошибка при загрузке данных: {e}")
            raise

    def delete_user(self, email: str):
        delete_query = f"DELETE FROM client WHERE email = '{email}';"

        try:
            with self._get_connection() as conn:
                conn.autocommit = True
                with conn.cursor() as cur:
                    cur.execute(delete_query)

        except Exception as e:
            logger.error(f"Ошибка при удалении документов: {e}")
            raise
