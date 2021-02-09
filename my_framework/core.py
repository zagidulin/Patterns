import views
from urllib.parse import unquote


class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        print(environ)
        path = environ['PATH_INFO']
        if path[-1] != '/':
            path += '/'

        method = environ[ 'REQUEST_METHOD' ]
        query_string = environ[ 'QUERY_STRING' ]
        # получаем параметры запроса, направленного методом POST
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        
        # получаем параметры запроса, направленного методом GET
        request_params = self.parse_input_data(query_string)
        
        if path in self.routes:
            view = self.routes[path]
            request = {}
            request['method'] = method
            request['data'] = data
            request['request_params'] = request_params
            if request_params:
                print(f'Получен GET-запрос: {request_params}')
            for front in self.fronts:
                front(request)
            code, body = view(request)
            start_response(code, [('Content-Type', 'text/html')])
            return body
        else:
            view = views.not_found_404_view
            code, body = view()
            start_response(code, [('Content-Type', 'text/html')])
            return body
        
    def parse_input_data (self, data: str):
        result = {}
        if data:
        # разделение параметров по '&'
            params = data.split('&')
            for item in params:
            # разделение на ключ и значение по '='
                k, v = item.split('=')
                result[k] = v
        return result

    def get_wsgi_input_data(self, environ):
        content_length_data = environ.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes):
        result = {}
        print(data)
        if data:
            data_str = data.decode(encoding='utf-8')
            data_str = unquote(data_str)
            result = self.parse_input_data(data_str)
        return result
