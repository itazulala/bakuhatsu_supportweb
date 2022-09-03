from django.urls import path
from .views import ArticleDetail, ArticleList, ArticleSearchList, CommentDetail, ThreadCreate, CommentCreate

urlpatterns = [
  path('list/', ArticleList.as_view(), name='contents_list'),
  path('searchlist/', ArticleSearchList.as_view(), name='search_contents_list'),
  path('<int:pk>/article/', ArticleDetail.as_view(), name='contents_detail'),
  path('comment/create/', ThreadCreate.as_view(), name='thread_create'),
  path('comment/<int:pk>/detail/', CommentDetail.as_view(), name='comment_detail'),
  path('comment/ditail/add/', CommentCreate.as_view(), name='comment_create'),
]