import json

from io import BytesIO
from socketserver import ThreadingTCPServer
from http.server import HTTPServer, BaseHTTPRequestHandler

from urls import urls_items


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = self.router()('get')
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        body = json.loads(body.decode())
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = self.router()('post', body)
        response = BytesIO(json.dumps(response).encode())
        self.wfile.write(response.getvalue())

    def router(self):
        return urls_items.get(self.path)


class ThreadingServer(ThreadingTCPServer, HTTPServer):
    pass


if __name__ == '__main__':
    server = ThreadingServer(('localhost', 8000), RequestHandler)
    server.serve_forever()
