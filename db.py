import io
import json
from abc import ABC, abstractmethod


class Connection(ABC):
    """Connection abstract class"""
    @abstractmethod
    def get_conn(self):
        pass


class InMemConnection(Connection):
    """In-memory connection object"""
    def get_conn(self) -> io.BytesIO:
        connection = io.BytesIO()
        connection.write(json.dumps({}).encode())
        return connection

    @staticmethod
    def read(conn: io.BytesIO) -> dict:
        """
        Read from db
        :param conn: conection instance
        :return: db data. Example: {"1": "a", "2": "b"}
        """
        data = conn.getvalue()
        data = json.loads(data.decode())
        return data

    @staticmethod
    def save(conn: io.BytesIO, data: dict):
        """
        Sace to db
        :param conn: conection instance
        :param data: data to save. Example: {"1": "a", "2": "b"}
        """
        conn.seek(0)
        conn.write(json.dumps(data).encode())