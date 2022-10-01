from django.urls import path
from .views import ToolsList

urlpatterns = [
    path('list/', ToolsList.as_view(), name='tools_list'),
]
