from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from django.shortcuts import redirect
from rango.forms import PageForm
from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    # order the categories on web app by number of likes (descending) and get top 5
    category_list = Category.objects.order_by('-likes')[:5]
    # order pages on web app by number of views and get top 5
    page_list = Page.objects.order_by('-views')[:5]
    # context to be passed to the template (ie index.html)
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    # display this template on the web app page using the context above
    # note: render() takes in the user’s request, the template filename, and the context dictionary as inputs
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    # context to be passed to the template (ie about.html)
    context_dict = {
        'boldmessage': 'This tutorial has been put together by Aubrey.'}
    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
    # context to be passed to the template (ie category.html)
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)


def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=True)
            print(cat, cat.slug)
            return redirect('/rango/')
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    if category is None:
        return redirect('/rango/')
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)
