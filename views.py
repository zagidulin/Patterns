from my_framework import templator


def index_view(request):
    print(request)
    main = templator.render('index.html', object_list=request['main'], pages=request['pages'])
    return '200 OK', [bytes(main, encoding = 'utf-8')]


def courses_view(request):
    print(request)
    courses = templator.render('courses.html', object_list=request['courses'], pages=request['pages'])
    return '200 OK', [bytes(courses, encoding = 'utf-8')]


def contacts_view(request):
    print(request)
    if request['method'] == 'POST':
        data = request['data']
        name = data['name'] if data['name'] else 'no name left'
        email = data['email']
        title = data['title']
        message = data['message']
        msg = f'От пользователя {name} ({email}) по теме: "{title}" получено сообщение: "{message}"'
        print(msg)
        with open('messages.txt', 'a') as f:
            f.write(msg)
            f.write('\n')
        contacts = templator.render('contacts.html', pages=request['pages'])
    else:
        contacts = templator.render('contacts.html', pages=request['pages'])
    return '200 OK', [bytes(contacts, encoding = 'utf-8')] 


def not_found_404_view():
    return '404 Error', [b'404: Page Not Found']


# вариант на классах
class About:
    def __call__(self, request):
        print(request)
        return '200 OK', [b'<h1>About us</h1>']
