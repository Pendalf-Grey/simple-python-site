from http.server import BaseHTTPRequestHandler, HTTPServer


PORT = 8000


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        html = """<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Python Site</title>
  <style>
    body { margin: 0; min-height: 100vh; display: grid; place-items: center; font-family: Arial, sans-serif; background: #f4f7fb; color: #1d2733; }
    main { max-width: 680px; padding: 48px 24px; text-align: center; }
    h1 { margin: 0 0 12px; font-size: clamp(36px, 7vw, 68px); }
    p { margin: 0; font-size: 20px; line-height: 1.5; }
  </style>
</head>
<body>
  <main>
    <h1>Python Site</h1>
    <p>Простой одностраничный сайт на Python.</p>
  </main>
</body>
</html>"""
        self.wfile.write(html.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Server running at http://localhost:{PORT}")
    server.serve_forever()
