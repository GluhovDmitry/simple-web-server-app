from db import InMemConnection
from loguru import logger

connection = InMemConnection()
conn = connection.get_conn()


class TransactionHandlers:
    @staticmethod
    def commit(table_data):
        InMemConnection.save(conn, table_data)

    @staticmethod
    def rollback(backup):
        InMemConnection.save(conn, backup)

    @staticmethod
    def begin():
        table_data = InMemConnection.read(conn)
        return table_data


def atomic(func):
    def wrapper(*args, **kwargs):
        backup = TransactionHandlers.begin()
        resp = {}
        try:
            resp = func(*args, **kwargs)
        except Exception as e:
            logger.error(str(e))
            TransactionHandlers.rollback(backup)
        else:
            TransactionHandlers.commit(resp)
        return resp
    return wrapper


class CRUDHandlers:
    @staticmethod
    def select():
        return InMemConnection.read(conn)

    @staticmethod
    @atomic
    def insert(data):
        table_data = InMemConnection.read(conn)
        last_id = 0
        if table_data:
            last_id = list(table_data.keys())[-1]
        table_data.update({int(last_id)+idx+1: value for idx, value in enumerate(data)})
        return table_data

    @staticmethod
    @atomic
    def delete(ids):
        table_data = InMemConnection.read(conn)
        for idx in ids:
            table_data.pop(str(idx))
        return table_data






