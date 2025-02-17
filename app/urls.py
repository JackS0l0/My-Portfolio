from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from main import views as mainviews
from articles import views as articleviews
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('',mainviews.index,name='index'),
    path('about_me/',mainviews.aboutme,name='about'),
    path('order_now/',mainviews.order,name='order'),
    path('contact_with_me/',mainviews.contact,name='contact'),
    path('article/<str:slug>/',articleviews.ArticlesDetailView.as_view(),name='post'),
    path('article_filter/<str:slug>/',articleviews.ArticlesFilterList.as_view(),name='filter'),
    path('articles/',articleviews.ArticlesList.as_view(),name='alllist'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>", mainviews.set_language, name="set-language"),
]