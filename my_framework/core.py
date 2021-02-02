class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        print(environ)
        path = environ['PATH_INFO']
        if path[-1] != '/':
            path += '/'
        if path in self.routes:
            view = self.routes[path]
        else:
            view = not_found_404_view
        request = {}
        for front in self.fronts:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return body
