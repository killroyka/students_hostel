from django.contrib import admin

from .models import News, NewsImage


class NewsImageInline(admin.TabularInline):
    model = NewsImage


@admin.register(News)
class NewsManager(admin.ModelAdmin):
    inlines = [
        NewsImageInline,
    ]
