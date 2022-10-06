from django.urls import path
from .views import ToolsList, ToolsDetail

urlpatterns = [
    path('list/', ToolsList.as_view(), name='tools_list'),
    path('<int:pk>/detail/', ToolsDetail.as_view(), name='tools_detail'),
    # path('<int:pk>/execution/', ToolsDetail.as_view(), name='tools_execution'),
]
