#!/usr/bin/env python3
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote

host = "localhost"


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        text = unquote(self.path)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(text, "utf-8"))

    def do_POST(self):
        length = int(self.headers.get("Content-Length"))
        data = self.rfile.read(length)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    print("Server started")
    port = int(sys.argv[1])
    webServer = HTTPServer((host, port), MyServer)
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
