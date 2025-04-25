from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Blog
from django.views.generic import ListView, DetailView
from news.models import News


class IndexView(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'item_list'

    def get_context_data(self, **kwargs):
        content = super(IndexView, self).get_context_data()
        news_list = News.objects.all()
        content['news_list'] = news_list