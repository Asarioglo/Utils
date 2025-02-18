from http.server import BaseHTTPRequestHandler, HTTPServer
import argparse

class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Echo back the request path in the response
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(f"Echo: {self.path}".encode("utf-8"))

    def do_POST(self):
        # Echo back the posted data in the response
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Echo: ")
        self.wfile.write(post_data)

    def log_message(self, format, *args):
        # Suppress logging to keep the output clean``
        return

def run(server_class=HTTPServer, handler_class=EchoHandler, port=8080):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting echo server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Echo Server")
    parser.add_argument(
        "--port", type=int, default=8080, help="Port to run the HTTP server on (default: 8080)"
    )
    args = parser.parse_args()
    run(port=args.port)