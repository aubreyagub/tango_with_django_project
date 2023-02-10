from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    # context to be passed to the template (ie index.html)
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # display this template on the web app page using the context above 
    # note: render() takes in the user’s request, the template filename, and the context dictionary as inputs
    return render(request, 'rango/index.html', context=context_dict)


def about(request): 
    context_dict = {'boldmessage': 'This tutorial has been put together by Aubrey.'}
    return render(request, 'rango/about.html', context=context_dict)

    # test