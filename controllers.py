import time

from handlers import CRUDHandlers


def insert(method: str, request_data: dict) -> dict:
    """
    Insert data controller
    :param method: http method
    :param request_data: request data. Example: {"data": ["a", "b"]}
    :return: db data
    """
    if method == 'post':
        data = request_data.get('data', {})
        result = CRUDHandlers.insert(data)
        return result


def select(method: str) -> dict:
    """
    Select data controller
    :param method: http method
    :return: db data
    """
    if method == 'get':
        result = CRUDHandlers.select()
        return result


def delete(method, request_data: dict) -> dict:
    """
    Delete data controller
    :param method: http method
    :param request_data: {"ids": [1, 3, 5]}
    :return: db data
    """
    if method == 'post':
        time.sleep(1000)
        ids = request_data.get('ids', [])
        result = CRUDHandlers.delete(ids)
        return result