from django.contrib import admin
from .models import Category, Tag, Article, Request


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Article, ArticleAdmin)