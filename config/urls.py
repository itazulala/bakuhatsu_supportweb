from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import TopPage, PrivacyPolicy


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', TopPage.as_view(), name='index'),
   path('privacypolicy', PrivacyPolicy.as_view(), name='privacy_policy'),
   path('faq/', include('faq.urls'), name='faq'),
   path('contents/', include('contents.urls'), name='contents'),
   path('information/', include('information.urls'), name='information'),
   path('contact/', include('contact.urls'), name='contact'),
   path('markdownx/', include('markdownx.urls')),
   path('api/', include('api.urls'), name='api'),
   path('tools/', include('tools.urls'), name='tools'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

