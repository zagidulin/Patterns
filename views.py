from my_framework import templator


def index_view(request):
    print('main')
    print(request)
    main = templator.render('index.html', object_list=request['main'])
    return '200 OK', [bytes(main, encoding = 'utf-8')]


def courses_view(request):
    print(request)
    courses = templator.render('courses.html', object_list=request['courses'])
    return '200 OK', [bytes(courses, encoding = 'utf-8')]


def not_found_404_view(request):
    print(request)
    return '404 Error', [b'404: Page Not Found']


# вариант на классах
class About:
    def __call__(self, request):
        print(request)
        return '200 OK', [b'<h1>About us</h1>']
