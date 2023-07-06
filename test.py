import requests

from loguru import logger

class HandlersTests:
    def test_select(self):
        url = 'http://127.0.0.1:8000/select/'
        resp = requests.get(url)
        return resp


    def test_insert(self):
        url = 'http://127.0.0.1:8000/insert/'
        resp = requests.post(url, json={"ids": [1, 3, 5]})
        return resp


    def test_delete(self):
        url = 'http://127.0.0.1:8000/delete/'
        resp = requests.post(url, json={"ids": [1, 3, 5]})
        return resp


class AtomicHandlersTests:
    def test_select(self):
        url = 'http://127.0.0.1:8000/aselect/'
        resp = requests.get(url)
        return resp

    def test_insert(self):
        url = 'http://127.0.0.1:8000/ainsert/'
        resp = requests.post(url, json={"ids": [1, 3, 5]})
        return resp

    def test_delete(self):
        url = 'http://127.0.0.1:8000/adelete/'
        resp = requests.post(url, json={"ids": [1, 3, 5]})
        return resp


if __name__ == '__main__':
    classic = HandlersTests()

    resp = classic.test_insert()
    logger.info(resp.json())
    resp = classic.test_select()
    logger.info(resp.json())
    resp = classic.test_delete()
    logger.info(resp.json())
