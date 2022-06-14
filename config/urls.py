from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import TopPage
from .views import FaqList
from .views import FaqDetail

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', TopPage.as_view(), name='index'),
   path('faq/list', FaqList.as_view(), name='faq/list'),
   path('faq/detail', FaqDetail.as_view(), name='faq/detail'),
   path('faq/', include('faq.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
