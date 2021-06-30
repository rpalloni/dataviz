from http.server import HTTPServer, CGIHTTPRequestHandler

# https://docs.python.org/3/library/http.server.html#http.server.CGIHTTPRequestHandler
# defaults dir to treat as containing CGI scripts ['/cgi-bin', '/htbin']
# add folder
CGIHTTPRequestHandler.cgi_directories = ['/core']
srv = HTTPServer

httpd = srv(('localhost', 8000), CGIHTTPRequestHandler)
print('Serving HTTP...')
httpd.serve_forever()
