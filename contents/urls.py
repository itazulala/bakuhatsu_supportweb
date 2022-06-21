from django.urls import path
from .views import ArticleDetail
from .views import ArticleList

urlpatterns = [
  path('<int:pk>/article/', ArticleDetail.as_view(), name='contents_detail'),
  path('list/', ArticleList.as_view(), name='contents_list'),
]