from my_framework import core
import views


# urlpatterns
routes = {
    '/': views.index_view,
    '/courses/': views.courses_view,
    '/about/': views.About(),
}


# Front controllers
def courses_front(request):
    request['courses'] = [
                        {'name': 'Course-1', 'href': '#'},
                        {'name': 'Course-2', 'href': '#'}
    ]


def main_front(request):
    request['main'] = {
                    'hot_offers': [('offer-1', '#'), ('offer-2', '#'), ('offer-3', '#')],
                    'news': [('news-1', '#'), ('news-2', '#'), ('news-3', '#')]
    }


fronts = [courses_front, main_front]


application = core.Application(routes, fronts)
