import psycopg2
from psycopg2.extras import RealDictCursor
from repositories.admin_base import DataBase
import datetime
from uuid import UUID
import logging

logger = logging.getLogger(__name__)


class ClientConnection(DataBase):
    def create_user(self, first_name: str, last_name: str, birth_date: datetime.date, email: str):
        insert_query = f"""INSERT INTO client (first_name, last_name, birth_date, email) VALUES ('{first_name}', 
        '{last_name}', '{birth_date}', '{email}');"""

        try:
            with self._get_connection() as conn:
                conn.autocommit = True
                with conn.cursor() as cur:
                    cur.execute(insert_query)
        except Exception as e:
            logger.error(f"Ошибка при загрузке данных: {e}")
            raise

    def get_levels(self):
        return DataBase.get_all_data(self, table='levels')

    def get_my_membership(self, client_id: UUID):
        query = f"""SELECT start_date, levels.name, status FROM gym_membership
                INNER JOIN levels ON levels.id = gym_membership.level
                WHERE id_client = '{client_id}';"""

        try:
            with self._get_connection() as conn:
                conn.autocommit = True
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute(query)
                    ans = cur.fetchall()
                    return ans
        except psycopg2.Error as e:
            logger.error(f"Ошибка в получении абонемента: {e}")
            return []

    def new_membership(self, client_id: UUID, level: int, start_date: datetime.date):
        insert_query = f"""INSERT INTO gym_membership (id_client, created_date, start_date, level, status) 
                        VALUES %s;"""

        try:
            with self._get_connection() as conn:
                conn.autocommit = True
                with conn.cursor() as cur:
                    cur.execute(insert_query, (client_id, datetime.date.today(), start_date, level, 'active'))
        except Exception as e:
            logger.error(f"Ошибка при загрузке данных: {e}")
            raise

    def update_profile(self, client_id: UUID, first_name: str, last_name: str, birth_date: datetime.date, email: str):
        query = f"""UPDATE client SET first_name = '{first_name}', last_name = '{last_name}', 
                birth_date = '{birth_date}', email = '{email}'
                WHERE id = '{client_id}';"""

        try:
            with self._get_connection() as conn:
                conn.autocommit = True
                with conn.cursor() as cur:
                    cur.execute(query)
        except Exception as e:
            logger.error(f"Ошибка при обновлении данных: {e}")

    def get_profile(self, client_id: UUID):
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