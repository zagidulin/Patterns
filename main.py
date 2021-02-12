from my_framework import core
import views


# urlpatterns
routes = {
    '/': views.index_view,
    '/categories/': views.categories_view,
    '/about/': views.About(),
    '/contacts/': views.contacts_view,
    '/category/': views.category_view,
}


# Front controllers
def main_front(request):
    request['main'] = {
                    'hot_offers': [('offer-1', '#'), ('offer-2', '#'), ('offer-3', '#')],
                    'news': [('news-1', '#'), ('news-2', '#'), ('news-3', '#')]
    }


def categories_front(request):
    request['categories'] = [
                        {'category': 'Музыка', 'href': '/category/', 'alias': 'music'},
                        {'category': 'Танцы', 'href': '/category/', 'alias': 'dance'},
                        {'category': 'Йога', 'href': '/category/', 'alias': 'yoga'},
                        {'category': 'Ремёсла', 'href': '/category/', 'alias': 'handcraft'},
    ]


def courses_front(request):
    request['courses'] = {
                        'music': [('music-course-1', '#'), ('music-course-2', '#'), ('music-course-3', '#')],
                        'dance': [('dance-course-1', '#'), ('dance-course-2', '#'), ('dance-course-3', '#')],
                        'yoga': [('yoga-course-1', '#'), ('yoga-course-2', '#'), ('yoga-course-3', '#')],
                        'handcraft': [('handcraft-course-1', '#'), ('handcraft-course-2', '#'), ('handcraft-course-3', '#')],
    }


fronts = [categories_front, main_front, courses_front]


application = core.Application(routes, fronts)
