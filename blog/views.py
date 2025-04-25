from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Blog
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'item_list'
