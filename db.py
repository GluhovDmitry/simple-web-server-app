import io
import json
from abc import ABC, abstractmethod


class Connection(ABC):
    @abstractmethod
    def get_conn(self):
        pass


class InMemConnection(Connection):
    def get_conn(self):
        connection = io.BytesIO()
        connection.write(json.dumps({}).encode())
        return connection

    @staticmethod
    def read(conn):
        data = conn.getvalue()
        data = json.loads(data.decode())
        return data

    @staticmethod
    def save(conn, data):
        conn.seek(0)
        conn.write(json.dumps(data).encode())