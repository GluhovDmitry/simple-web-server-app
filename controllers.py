import time

from handlers import CRUDHandlers


def insert(method, request_data: dict):
    if method == 'post':
        data = request_data.get('data', {})
        result = CRUDHandlers.insert(data)
        return result


def select(method):
    if method == 'get':
        result = CRUDHandlers.select()
        return result


def delete(method, request_data: dict):
    if method == 'post':
        time.sleep(1000)
        ids = request_data.get('ids', [])
        result = CRUDHandlers.delete(ids)
        return result