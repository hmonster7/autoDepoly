from django.contrib import admin

# Register your models here.
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', )
    list_display_links = ('pk', 'title')


admin.site.register(News, NewsAdmin)