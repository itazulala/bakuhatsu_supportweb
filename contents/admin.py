from django.contrib import admin
from .models import Category, Tag, Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'draft')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)

