import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
       # pages about Python
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/',
         'views':10},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'views':9},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'views':8}]


    # pages about Django
    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views':14},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'views':13},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views':12}]

    # pages on other topics
    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/',
         'views':6},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org',
         'views':5}]

    # note: add more categories on this area when required

    # dictionary of dictionaries of all categories
    cats = {'Python': {'pages': python_pages, 'likes': 64, 'views': 128},
            'Django': {'pages': django_pages, 'likes': 32, 'views': 64},
            'Other Frameworks': {'pages': other_pages, 'likes': 16, 'views': 32}}


    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, title=p['title'], url=p['url'], views=p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

# functions used above to add the pages and categories 
def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = likes;
    c.views = views;
    c.save()
    return c

# note: this is where code execution begins
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()