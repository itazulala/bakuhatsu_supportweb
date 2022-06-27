from django.contrib import admin
from .models import Category
from .models import Tag
from .models import Article

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)



