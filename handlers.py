from db import InMemConnection
from loguru import logger

connection = InMemConnection()
conn = connection.get_conn()


class TransactionHandlers:
    """Transaction object"""
    @staticmethod
    def commit(table_data):
        """
        Commit transaction
        :param table_data:
        """
        InMemConnection.save(conn, table_data)

    @staticmethod
    def rollback(backup):
        """
        Rollback changes
        :param backup: backup db data. Example {"1": "a", "2": "b"}
        """
        InMemConnection.save(conn, backup)

    @staticmethod
    def begin():
        """
        Save backup
        :return: backup db data. Example: {"1": "a", "2": "b"}
        """
        table_data = InMemConnection.read(conn)
        return table_data


def atomic(func):
    """Decorator that provides atomic transactions"""
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
    """CRUD object"""
    @staticmethod
    def select():
        """
        Select logic
        :return:
        """
        return InMemConnection.read(conn)

    @staticmethod
    @atomic
    def insert(data: list) -> dict:
        """
        Insert logic
        :param data: data to save. Example ["a", "b"]
        :return: db data. Example {"1": "a", "2": "b"}
        """
        table_data = InMemConnection.read(conn)
        last_id = 0
        if table_data:
            last_id = list(table_data.keys())[-1]
        table_data.update({int(last_id)+idx+1: value for idx, value in enumerate(data)})
        return table_data

    @staticmethod
    @atomic
    def delete(ids: list) -> dict:
        """
        Insert logic
        :param ids: data ids to delete. Example [1, 2]
        :return: db data. Example {"3": "a", "4": "b"}
        """
        table_data = InMemConnection.read(conn)
        for idx in ids:
            table_data.pop(str(idx))
        return table_data






