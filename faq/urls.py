from django.urls import path
from .views import ArticleDetail

urlpatterns = [
  path('<int:pk>/article/', ArticleDetail.as_view(), name='article_detail'),
]