from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

server_address = ("0.0.0.0", 8443)

httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(
    certfile="localhost+3.pem",
    keyfile="localhost+3-key.pem"
)

httpd.socket = context.wrap_socket(
    httpd.socket,
    server_side=True
)

print("Servidor HTTPS iniciado")
print("https://localhost:8443")
print("https://192.168.15.109:8443")

httpd.serve_forever()

