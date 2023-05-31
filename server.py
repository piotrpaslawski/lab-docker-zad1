import http.server
import socketserver
import datetime
import requests


server_host = "localhost"
server_port = 8000
server_full_address = f"{server_host}:{server_port}"


class ServerController(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        current_time = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        print(f"{current_time} - page opened on {server_full_address}")

    def generate_page(self, ip_address, client_time, client_timezone):
        return f"""
        <html>
        <head>
            <title>Very nice server</title>
        </head>
        <body>
            <h1>Very nice server by Piotr Paslawski</h1>
            <p>Your IP Address: {ip_address}</p>
            <p>Your time: {client_time} {client_timezone}</p>
        </body>
        </html>
        """

    def do_GET(self):
        client_ip = self.get_ip_address(self)
        client_time, client_timezone = self.get_time_timezone()
        response_content = self.generate_page(client_ip, client_time, client_timezone)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(response_content, "utf-8"))

    def get_ip_address(self, request_handler):
        ip_address = requests.get('https://checkip.amazonaws.com').text.strip()
        return ip_address

    def get_time_timezone(self):
        client_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client_timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        return client_time, client_timezone


with socketserver.TCPServer((server_host, server_port), ServerController) as server:
    print(f"Hello, World! Server made by Piotr Paslawski and started on {server_full_address}. Welcome ;-)")
    server.serve_forever()
