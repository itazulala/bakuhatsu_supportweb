from django.urls import path
from .views import ArticleDetail, ArticleList

urlpatterns = [
    path('list/', ArticleList.as_view(), name='faq_list'),
    path('<int:pk>/article/', ArticleDetail.as_view(), name='faq_detail'),
]
