import requests
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

source_url = "https://127.0.0.1:2999/liveclientdata/activeplayer"

HOST = '0.0.0.0'
PORT = 5000

class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            response = requests.get(source_url, verify=False)
            if response.status_code == 200:
                data = response.json()
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())
            else:
                self.send_error(response.status_code, f"Error al cargar datos: {response.status_code}")
        except Exception as e:
            self.send_error(500, e)

def run(server_class=HTTPServer, handler_class=ProxyHTTPRequestHandler):
    server_address = (HOST, PORT)
    httpd = server_class(server_address, handler_class)
    print(f"proxy server escuchando en http://{HOST}:{PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
