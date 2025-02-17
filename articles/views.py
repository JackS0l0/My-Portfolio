from django.shortcuts import render
from .models import Articles,Categories
from app.utils import common_data
from django.views.generic import DetailView,ListView
class ArticlesDetailView(DetailView):
    model=Articles
    template_name='post.html'
    context_object_name='articles'
    def get_context_data(self, **kwargs):
        context=super(ArticlesDetailView,self).get_context_data(**kwargs)
        context['title']=f'{self.object.name} - Javidan Babayev'
        context.update(common_data())
        return context
class ArticlesFilterList(ListView):
    model=Articles
    template_name='filter.html'
    context_object_name='articles'
    paginate_by = 15
    def get_queryset(self):
        slug=self.kwargs.get('slug')
        category = Categories.objects.get(slug=slug)
        return Articles.objects.filter(cate=category).order_by('-date')
    def get_context_data(self, **kwargs):
        category = Categories.objects.get(slug=self.kwargs.get('slug'))
        context=super(ArticlesFilterList,self).get_context_data(**kwargs)
        context['title']=f'{category.name} - Javidan Babayev'
        context.update(common_data())
        return context
class ArticlesList(ListView):
    model=Articles
    template_name='filter.html'
    context_object_name='articles'
    paginate_by = 15
    def get_context_data(self, **kwargs):
        context=super(ArticlesList,self).get_context_data(**kwargs)
        context['title']='Bütün məqalələr - Javidan Babayev'
        context.update(common_data())
        return context