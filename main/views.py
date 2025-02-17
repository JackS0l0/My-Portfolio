from django.shortcuts import render
from app.utils import common_data
from articles.models import Articles
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
def index(request):
    data = common_data()
    context={
        'title':'Javidan Babayev',
        'articles':Articles.objects.all().order_by('-date')[4:12],
    }
    data.update(context)
    return render(request,'index.html',data)
def aboutme(request):
    data = common_data()
    context={
        'title':'Haqqımda - Javidan Babayev',
    }
    data.update(context)
    return render(request,'about.html',data)

def order(request):
    data = common_data()
    context={
        'title':'Haqqımda - Javidan Babayev',
    }
    data.update(context)
    return render(request,'order.html',data)
def contact(request):
    data = common_data()
    context={
        'title':'Haqqımda - Javidan Babayev',
    }
    data.update(context)
    return render(request,'contact.html',data)