def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    body = environ['QUERY_STRING'].split("&")
    body = "\r\n".join(body).encode()
    return [body]

