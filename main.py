from http.server import SimpleHTTPRequestHandler, HTTPServer

port = 5000

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

with HTTPServer(('0.0.0.0', port), MyHandler) as httpd:
    print(f'Server running at http://localhost:{port}')
    httpd.serve_forever()