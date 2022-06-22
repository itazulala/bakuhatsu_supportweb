from django.contrib import admin
from .models import Category
from .models import Tag
from .models import Article
from .models import MarkdownFile


class SampleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'good_count',)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article, SampleAdmin)
admin.site.register(MarkdownFile)
