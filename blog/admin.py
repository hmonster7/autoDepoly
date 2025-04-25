from django.contrib import admin

# Register your models here.
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', )
    list_display_links = ('pk', 'name')


admin.site.register(Blog, BlogAdmin)