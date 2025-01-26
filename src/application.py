from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

hostName = "localhost"
serverPort = 8080


class MyRequests(BaseHTTPRequestHandler):
    """Класс для обработки входящих запросов"""

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        html_dir = Path(__file__).parent.joinpath('html')
        file_path = html_dir / "contacts_page.html"

        if file_path.exists():
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            self.wfile.write(content.encode("utf-8"))
        else:
            self.send_error(404, "HTML Страница не найдена")


def run(server_class=HTTPServer, handler_class=MyRequests, port=serverPort):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on port {port}')
    httpd.serve_forever()
